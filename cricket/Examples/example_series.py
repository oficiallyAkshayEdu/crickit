import sys

import cricket
from cricket.Logger import *

scriptlog.setLevel(logging.WARNING)
scriptlog.info("Imports Complete")
scriptlog.info("Starting Example Script. Logger started")
matchlog.setLevel(logging.WARNING)

# run script from command line
if len(sys.argv) > 1:
    t1 = sys.argv[-1].title()
    t2 = sys.argv[-2].title()
else:
    t1 = "India"
    t2 = "Pakistan"

matchlog.info("Starting a __match between {} and {}".format(t1, t2))

## creates __match object
match = cricket.play_match(t1, t2)

matchlog.debug("Winner {} scored {} runs. Loser {} scored {} runs ".format(match.winner, match.winner.runs, match.loser,
                                                                           match.loser.runs))

matchlog.info("Match Complete. Quitting. Bye! <3")
# __match.toss.name = "Hello"
# print(__match.toss.name)
sys.exit()

# TODO rename main git repo
