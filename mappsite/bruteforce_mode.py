from base_class import *


class BruteforceScan(WrapperScan):
    PATH_LIMIT = 20
    CHAR_SET = list(string.ascii_lowercase + string.ascii_uppercase + string.digits) \
               + [c for c in "<>-.#@*^?%$=!+&"]

    # to reimplement iteratively TO-FIX
    def gen_list(self, paths_list: list, length, partial_string: str):
        if length == 0:
            for char in self.CHAR_SET:
                paths_list.append(partial_string + char)
            return
        else:
            for char in self.CHAR_SET:
                self.gen_list(paths_list, length - 1, partial_string + char)

    def bruteforce_attack(self, parent, paths_list: [str], depth):
        if depth == self.PATH_LIMIT:
            return

        success = 0
        chars_num = len(self.CHAR_SET)
        inc = chars_num ** (self.PATH_LIMIT - depth)

        for i in range(chars_num ** depth):
            index = i * inc - 1
            # TO-FIX / TEST what is path -- MUST PASS partial link to tree append and then parent node
            path = paths_list[index][:depth]
            outcome, red_tree = test_connection(parent, path)

            if red_tree is not None:
                tree_append(self.website_fs, parent, red_tree)
                success += 1
            elif outcome:
                print(f"\nNew dir found: {parent.data}/{path}")
                success += 1
                tree_append(self.website_fs, parent, path)

        self.bruteforce_attack(parent, paths_list, depth + 1)

    def bruteforce_mode(self):
        paths_list = []
        depth = 0
        url_list = [self.website_fs.identifier]
        self.gen_list(paths_list, self.PATH_LIMIT, '')

        while True:
            bruteforce_pool = th.ThreadPoolExecutor(max_workers=self.MAX_THRD)
            futures = []
            stop_flag = thr.Event()
            for url in url_list:
                futures.append(bruteforce_pool.submit(self.bruteforce_attack, url, paths_list, 0))
            action = handle_user_input(futures, stop_flag)
            url_list = list(self.website_fs.filter_nodes(lambda x: self.website_fs.depth(x) == depth))
            depth += 1
