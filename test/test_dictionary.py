import multiprocessing
import unittest
import mappsite.dictionary_mode
import treelib as tr
import os
import threading as thr
import time
import concurrent.futures as th


class TestDictionary(unittest.TestCase):

    def setUp(self):
        self.DictionaryScan = mappsite.dictionary_mode.DictionaryScan("https://www.polimi.it")

    def tearDown(self):
        # os.remove('dictionary_scan.log')
        pass

    def test_load_batch(self):
        word = mappsite.dictionary_mode.next_word("../dictionaries/wordlist_test.txt")
        print(next(word) + next(word) + next(word))

    def test_dictionary_attack(self):
        tree = tr.Tree()
        node = tree.create_node("https://stackoverflow.com/questions/53920372/", "https://stackoverflow.com/questions"
                                                                                 "/53920372/")

        # stop_flag = multiprocessing.Value('i', False)
        # stop_flag_lock = thr.Lock()
        stop_flag = thr.Event()

        pool = th.ThreadPoolExecutor(max_workers=5)
        pool.submit(
            self.DictionaryScan.dictionary_attack, node, "../dictionaries/wordlist_test.txt", stop_flag
        )
        time.sleep(1)
        stop_flag.set()
        # with stop_flag_lock:
        #     stop_flag.value = 1
        tree.show()

    def test_dictionary_mode(self):
        # self.DictionaryScan.dictionary_mode("../dictionaries/wordlist_test.txt")
        pass


if __name__ == '__main__':
    unittest.main()
