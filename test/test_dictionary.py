import unittest
import mappsite.dictionary_mode
import treelib as tr
import os
import threading as thr
import time


class TestDictionary(unittest.TestCase):

    def setUp(self):
        self.DictionaryScan = mappsite.dictionary_mode.DictionaryScan("https://www.polimi.it")

    def tearDown(self):
        os.remove('dictionary_scan.log')
        pass

    def test_load_batch(self):
        batch = self.DictionaryScan.load_batch("../dictionaries/wordlist_test.txt", 0)
        print(batch)

    def test_dictionary_attack(self):
        stop_flag = thr.Event()
        tree = tr.Tree()
        node = tree.create_node("https://www.polimi.it", "https://www.polimi.it")
        self.DictionaryScan.dictionary_attack(node, "../dictionaries/wordlist_test.txt", stop_flag)
        time.sleep(5)
        stop_flag.set()
        tree.show()

    def test_dictionary_mode(self):
        self.DictionaryScan.dictionary_mode("../dictionaries/wordlist_test.txt")


if __name__ == '__main__':
    unittest.main()
