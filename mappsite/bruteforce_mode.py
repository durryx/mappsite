from helpers import *
import sys
import logging as log
import string
import concurrent.futures as th


class BruteforceScan:
    website_fs = None
    PATH_LIMIT = 20
    CHAR_SET = list(string.ascii_lowercase + string.ascii_uppercase + string.digits) \
               + [c for c in "<>-.#@*^?%$=!+&"]
    MAX_THRD = 10

    def __init__(self, website: str):
        sys.setrecursionlimit(5000)
        log.basicConfig(filename='app.log', filemode='w', level=log.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - dictionary scan -- %(message)s')
        # logger = log.getLogger(__name__)
        # logger.debug('This is a debug message')

        self.website_fs = tr.Tree()
        self.website_fs.create_node(website, website)

    # to reimplement iteratively TO-FIX
    def gen_list(self, paths_list: list, length, string):
        if length == 0:
            for char in self.CHAR_SET:
                paths_list.append(string + char)
        else:
            for char in self.CHAR_SET:
                self.gen_list(paths_list, length - 1, string + char)

    def bruteforce_attack(self, parent, paths_list, depth):
        if depth == self.PATH_LIMIT:
            return

        success = 0
        chars_num = len(self.CHAR_SET)
        inc = chars_num ** (self.PATH_LIMIT - depth)

        for i in range(chars_num ** depth):
            index = i * inc - 1
            path = paths_list[index][:depth]
            outcome, red_tree = test_connection(parent, path)

            if red_tree is not None:
                tree_append()
            elif outcome:
                print(f"\nNew dir found: {parent.data}/word")
                success += 1
                tree_append()

        self.bruteforce_attack(parent, paths_list, depth + 1)

    def bruteforce_mode(self, website):
        paths_list, depth = [], 0
        url_list = [website]
        self.gen_list(paths_list, self.PATH_LIMIT, '')

        while True:
            bruteforce_pool = th.ThreadPoolExecutor(max_workers=self.MAX_THRD)
            futures = []
            for url in url_list:
                futures.append(bruteforce_pool.submit(self.bruteforce_attack, url, paths_list, 0))
            handle_user_input(futures)
            url_list = list(self.website_fs.filter_nodes(lambda x: self.website_fs.depth(x) == depth))
            depth += 1
