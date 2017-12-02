import unittest

from crickit.match import *

from crickit.PlayCricket import *
from crickit.classes.teams import *


class TestCrickit(unittest.TestCase):

    def setup(self):
        pass

    def test_WinnerDeclaration(self):
        match = playMatch("India","Pakistan")
        result = declareMatchWinner(match)
        self.assertIsInstance(result, Teams)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()