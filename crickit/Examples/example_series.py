import crickit
from crickit.Logger import *
import os
import sys

scriptlog.setLevel(logging.WARNING)
scriptlog.info("Imports Complete")
scriptlog.info("Starting Example Script. Logger started")


if len(sys.argv) > 1:
    t1 = sys.argv[-1].title()
    t2 = sys.argv[-2].title()
else:
    t1 = "India"
    t2 = "Pakistan"


matchlog.info("Starting a match between {} and {}".format(t1, t2))
match = crickit.play_match(t1, t2)

print()
# print(match.__repr__)
print(match.loser.wicketsLost, match.winner.wicketsLost)
print(match.winner.runs, match.winner)
print(match.loser.runs, match.loser)
# print(len(crickit.Teams.allteamobjects))
# print(simulatedMatch.matches[1].winner.runs)
# print(simulatedMatch.matches[2].winner.runs)
# print(simulatedMatch.matches[3].winner.runs)


matchlog.info("Match Complete. Quitting. Bye! <3")
sys.exit()