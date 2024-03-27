import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from base_class import *
from helpers import *
from typing import Generator
import threading
from prompt_toolkit.patch_stdout import patch_stdout
import time

from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter
from queue import Queue

print = print_formatted_text


def next_word(file) -> Generator:
    with open(file, "r") as f:
        for line in f:
            yield line.strip('\n')


prompt_style = Style.from_dict(
    {
        # The 'rprompt' gets by default the 'rprompt' class. We can use this
        # for the styling.
        "rprompt": "bg:#ff0066 #ffffff",
    }
)


class DictionaryScan(WrapperScan):
    # indicating the max depth of the tree
    depth = 0
    futures = []
    # pause threads
    stop_flag = thr.Event()
    # generated events to be printed
    events_queue = Queue()
    # False if threads are working, True if they are done
    thread_status_flag = False
    run_print_events = True

    def handle_user_input(self):
        print_thread = threading.Thread(target=self.print_events, args=())
        print_thread.daemon = True
        print_thread.start()
        history = InMemoryHistory()
        command_completer = WordCompleter(['SWITCH', 'EXIT', 'SAVE', 'VIEW', 'SKIP', 'DICT',
                                           'CONTINUE', 'TOT_REQUESTS', 'HELP'])
        session = PromptSession(history=history, enable_history_search=True)

        while True:
            with patch_stdout():
                command = session.prompt(">",
                                         placeholder=HTML('<style color="#888888">(please type something)</style>'),
                                         rprompt=self.rprompt_text, bottom_toolbar=self.get_toolbar,
                                         refresh_interval=0.5,
                                         style=prompt_style, completer=command_completer)
            print(">%s" % command)
            history.append_string(command)
            self.execute_command(command)

    def print_events(self):
        one_thread_check = lambda proc: True if (proc.done()) else False
        while self.run_print_events:
            events = [self.events_queue.get() for _ in range(self.events_queue.qsize())]
            for event in events:
                print("[INFO] new link found: " + event)
            self.stop_flag.set()
            if all(map(one_thread_check, self.futures)):
                print("[INFO] all threads have finished ... ")
                self.thread_status_flag = True
                return
            time.sleep(3)

    def rprompt_text(self):
        # style based on success of entered program
        return [
            ("", " "),
            ("underline", "<rprompt>"),
            ("", " "),
        ]

    def get_toolbar(self):
        return "mappsite -- dictionary mode -- status {0} -- max depth: {1} -- requests rate: {2}".format(
            "Done" if self.thread_status_flag else "Working", self.depth, self.requests_rate)

    def execute_command(self, command):
        # create parent class with function to handle actions and other constructors/destructors
        match command:
            case InputCodes.CONTINUE:
                pass
            case InputCodes.SHUTDOWN:
                # call helper function to save session
                return
            case InputCodes.SKIP:
                # STOP means to start going another level deep
                # make the user select what directory to further investigate
                pass
            case InputCodes.PAUSE:
                # STOP means to start going another level deep
                # make the user select what directory to further investigate
                pass
            case InputCodes.SELECTOR:
                # do not analise a certain subdirectory
                pass

    def dictionary_attack(self, parent: tr.Node, file: str, stop_flag: thr.Event):
        success = 0
        timer = thr.Timer(self.MAX_TIME, lambda *args: None)
        with open(file) as f:
            num_lines = sum(1 for line in f)
        word = next_word(file)
        partial_link = link_cat(self.website_fs, parent)

        timer.start()
        while True:
            try:
                current_word = copy.deepcopy(next(word))
            except StopIteration:
                # load next file with .send or return if not possible
                word.close()
                return
            outcome, red_tree = test_connection(partial_link, current_word)
            if red_tree is not None:
                tree_append(self.website_fs, parent, red_tree)
                success += 1
            elif outcome:
                success += 1
                tree_append(self.website_fs, parent, current_word)

            if not timer.is_alive():
                """
                with stop_flag_lock:
                    if stop_flag.value:
                        return
                """
                if stop_flag.is_set():
                    return
                timer = thr.Timer(self.MAX_TIME, lambda *args: None)
                timer.start()
            self.total_requests.inc()

    def dictionary_mode(self, file):
        # skip this UI part if initialization indicates
        iter_links = [self.website_fs.root]
        # initialize variables with UI
        # auto mode
        #
        # dictionaries to be used
        # max timeout
        while True:
            self.thread_status_flag = False
            # find a way to check which node exploration has started, max_workers has to be benchmarked
            # exception FutureWarning
            dictionary_pool = th.ThreadPoolExecutor(max_workers=self.MAX_THRD)
            for node in iter_links:
                self.futures.append(dictionary_pool.submit(self.dictionary_attack, node, file, self.stop_flag))

            # after submitting work to threads enter the UI and give control to user
            self.handle_user_input()

            iter_links = iter(self.website_fs.filter_nodes(lambda x: self.website_fs.depth(x) == self.depth))
            self.depth += 1
