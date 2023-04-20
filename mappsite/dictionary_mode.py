from base_class import *
from helpers import *

def load_batch(file) -> str:
    # handle case where end of file is reached
    try:
        with open(file, "r") as f:
            for line in f:
                yield line
    except FileNotFoundError as e:
        logger = log.getLogger(__name__)
        logger.exception("dictionary file not found")
        print(e)
        raise SystemExit


class DictionaryScan(WrapperScan):
    STRIDE = 2000

    def next_word(self, file):
        with open(file, 'r') as f:
            yield next(f)

    # convert to python generator

    def dictionary_attack(self, parent: tr.Node, file: str, stop_flag: thr.Event):
        index, success = 0, 0
        batch: list = load_batch(file, index)
        partial_link = link_cat(self.website_fs, parent)

        while True:
            for index, word in enumerate(batch):
                # parent.data takes the used payload associated by the user to the node id
                # word[:-1] is necessary because it has a "\n" on the end
                outcome, red_tree = test_connection(partial_link, word[:-1])

                if red_tree is not None:
                    tree_append(self.website_fs, parent, red_tree)
                    success += 1
                elif outcome:
                    success += 1
                    tree_append(self.website_fs, parent, word)

            if stop_flag.is_set():
                return

            index += self.STRIDE
            batch = load_batch(file, index)

    def dictionary_mode(self, file):
        iter_links = [self.website_fs.root]
        depth = 0

        while True:
            # find a way to check which node exploration has started, max_workers has to be benchmarked
            # exception FutureWarning
            dictionary_pool = th.ThreadPoolExecutor(max_workers=self.MAX_THRD)
            futures = []
            stop_flag = thr.Event()
            for node in iter_links:
                futures.append(dictionary_pool.submit(self.dictionary_attack, node, file, stop_flag))
            action = handle_user_input(futures, stop_flag)

            # create parent class with function to handle actions and other constructors/destructors
            match action:
                case InputCodes.CONTINUE:
                    # print going another level deep
                    pass
                case InputCodes.SHUTDOWN:
                    return

                case InputCodes.STOP:
                    # STOP means to start going another level deep
                    # make the user select what directory to further investigate
                    pass

            iter_links = iter(self.website_fs.filter_nodes(lambda x: self.website_fs.depth(x) == depth))
            depth += 1
