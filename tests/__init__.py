import unittest
from .context import mappsite

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("ciao qua eseguo i testi quindi metti gli script")
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
