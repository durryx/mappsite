import unittest
import mappsite.dictionary_mode
import treelib as tr
import os


class TestDictionary(unittest.TestCase):

    def setUp(self):
        self.DictionaryScan = mappsite.dictionary_mode.DictionaryScan("https://www.polimi.it")

    def tearDown(self):
        # os.remove('dictionary_scan.log')
        pass

    def test_load_batch(self):
        batch = self.DictionaryScan.load_batch("../dictionaries/wordlist_test.txt", 0)
        print(batch)

    def test_dictionary_attack(self):
        pass

    def test_dictionary_mode(self):
        pass


if __name__ == '__main__':
    unittest.main()
