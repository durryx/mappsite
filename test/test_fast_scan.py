import multiprocessing
import unittest
import mappsite.fast_mode
import treelib as tr
import os
import threading as thr
import time
import concurrent.futures as th


class TestFastScan(unittest.TestCase):

    def SetUp(self):
        self.FastScan = mappsite.fast_mode.FastScan("https://www.scrapethissite.com/")

    def tearDown(self):
        pass

    def test_extract_from_link(self):
        urls = self.FastScan.extract_from_link("https://www.scrapethissite.com/")
        print(urls)

    def test_add_link_to_tree(self):

        pass

    def test_fast_scan_attack(self):
        pass

    def test_fast_scan_mode(self):
        pass


if __name__ == '__main__':
    unittest.main()
