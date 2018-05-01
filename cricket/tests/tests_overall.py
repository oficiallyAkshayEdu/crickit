from cricket import *
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


simulateCount = 100


def CompleteTest():
    # tests a single __match
    match = play_match("India", "Pakistan")

    # tests n simulated matches
    series = simulateMatches("India", "Pakistan", simulateCount)


if __name__ == '__main__':
    CompleteTest()
