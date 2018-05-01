from cricket import *
import os
import sys
import unittest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# import cricket


# from cricket.classes import *


class TestCrickit(unittest.TestCase):

    # def setup(self):
    #     pass

    def test_WinnerDeclaration(self):
        match = play_match("India", "Pakistan")
        series = simulateMatches("India", "Pakistan", 1000)
        self.assertIsInstance(match, Match)

    # def tearDown(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
