import concurrent.futures as th
import sys
import logging as log
from helpers import *

class DictionaryScan:
    website_fs = None
    STRIDE = 2000
    MAX_THRD = 10
    PATH_LIMIT = 20

    def __init__(self, website: str):
        sys.setrecursionlimit(5000)
        log.basicConfig(filename='app.log', filemode='w', level=log.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - dictionary scan -- %(message)s')
        # logger = log.getLogger(__name__)
        # logger.debug('This is a debug message')

        self.website_fs = tr.Tree()
        self.website_fs.create_node(website, website)

    def load_batch(self, file, index):
        try:
            with open(file, "r") as f:
                # reads lines between index and index + stride
                for _ in range(index):
                    next(file)
                batch = [next(file) for _ in range(self.STRIDE)]
            return batch
        except FileNotFoundError:
            logger = log.getLogger(__name__)
            logger.exception("dictionary file not found")
            raise SystemExit
        finally:
            f.close()

    def dictionary_attack(self, parent: tr.Node, file: str):
        index, success = 0, 0
        batch: list = self.load_batch(file, index)
        partial_link = link_cat(self.website_fs, parent, "")

        while True:
            for index, word in enumerate(batch):
                # parent.data takes the used payload associated by the user to the node id
                # word[:-1] is necessary because it has a "\n" on the end
                outcome, red_tree = test_connection(partial_link, word[:-1])

            # handle use input in order to break

                if red_tree is not None:
                    # tree_append
                elif outcome:
                    print(f"\nNew dir found: {parent.data}/{word}")
                    success += 1
                    # tree_append()

            index += self.STRIDE
            batch = self.load_batch(file, index)

        return True

    def automatic_mode(self, file):
        iter_links = [self.website_fs.root]
        depth = 0
        # lambda definition check_depth = lambda x,y: tree_structure.depth(x) == y

        while True:
            # find a way to check which node exploration has started, max_workers has to be benchmarked
            dictionary_pool = th.ThreadPoolExecutor(max_workers=self.MAX_THRD)
            for node in iter_links:
                # TO-FIX passing class to thread
                dictionary_pool.submit(self.dictionary_attack, node, file)
            handle_user_input(dictionary_pool)
            iter_links = iter(self.website_fs.filter_nodes(lambda x: self.website_fs.depth(x) == depth))
            depth += 1
