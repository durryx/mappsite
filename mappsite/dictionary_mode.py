import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from base_class import *
from helpers import *
from typing import Generator


def next_word(file) -> Generator:
    with open(file, "r") as f:
        for line in f:
            yield line.strip('\n')


class DictionaryScan(WrapperScan):
    futures = []
    stop_flag = thr.Event()

    def handle_user_input(self):
        one_thread_check = lambda proc: True if (proc.done()) else False
        while True:
            # user input and output - use ncurses?
            # stopping thread
            self.stop_flag.set()

            if all(map(one_thread_check, self.futures)):
                return [InputCodes.CONTINUE, None]

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
        iter_links = [self.website_fs.root]
        depth = 0

        while True:
            # find a way to check which node exploration has started, max_workers has to be benchmarked
            # exception FutureWarning
            dictionary_pool = th.ThreadPoolExecutor(max_workers=self.MAX_THRD)
            for node in iter_links:
                self.futures.append(dictionary_pool.submit(self.dictionary_attack, node, file, stop_flag))

            # after submitting work to threads enter the UI and give control to user
            code, action = self.handle_user_input()

            # create parent class with function to handle actions and other constructors/destructors
            match code:
                case InputCodes.CONTINUE:
                    # print going another level deep
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

            iter_links = iter(self.website_fs.filter_nodes(lambda x: self.website_fs.depth(x) == depth))
            depth += 1
