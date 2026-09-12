import unittest
from tool import recommend


class CompressionTests(unittest.TestCase):
    def test_selects_signal_appropriate_encoding(self):
        self.assertEqual(recommend([1, 1, 1, 2]), "run_length")
        self.assertEqual(recommend([1, 3, 5, 7]), "delta")
        self.assertEqual(recommend([1, 4, 2, 8]), "plain")


if __name__ == "__main__":
    unittest.main()
