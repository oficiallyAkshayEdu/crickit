import unittest,os,sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# import crickit

from crickit import *

class TestCrickit(unittest.TestCase):

    # def setup(self):
    #     pass

    def test_WinnerDeclaration(self):
        match = playMatch("India","Pakistan")
        # result = declareMatchWinner()
        result = declareMatchWinner(match)
        self.assertIsInstance(result, Teams)

    # def tearDown(self):
    #     pass

if __name__ == '__main__':
    unittest.main()