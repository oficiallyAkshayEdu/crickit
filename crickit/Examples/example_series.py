import sys

import crickit
from crickit.Logger import *

scriptlog.setLevel(logging.WARNING)
scriptlog.info("Imports Complete")
scriptlog.info("Starting Example Script. Logger started")

if len(sys.argv) > 1:
    t1 = sys.argv[-1].title()
    t2 = sys.argv[-2].title()
else:
    t1 = "India"
    t2 = "Pakistan"

matchlog.info("Starting a __match between {} and {}".format(t1, t2))
match = crickit.play_match(t1, t2)
print(match.winner.runs)
print(match.loser.runs)
matchlog.debug("Winner {} scored {} runs. Loser {} scored {} runs ".format(match.winner, match.winner.runs, match.loser, match.loser.runs))
# match.toss.__called_face


matchlog.info("Match Complete. Quitting. Bye! <3")
sys.exit()
