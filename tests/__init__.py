import unittest
from .context import *


def test_connection():
    print("test_connection with http://httpbin.org/relative-redirect/3 , no tree appending")
    url = "http://httpbin.org"
    mappsite.helpers.test_connection(url, "relative-redirect/2", None)
    # self.assertEqual(True, False)  # add assertion here

class MyTestCase(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
