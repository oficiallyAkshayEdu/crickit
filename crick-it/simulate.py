from PlayCricket import *
import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


class matchSimulator(Match):
    def __init__(self, MATCH_ID):

        self.MATCH_ID = MATCH_ID
        self.t1_wins = 0
        self.t2_wins = 0
        self.ties = 0
        super(matchSimulator, self).__init__(self.MATCH_ID)

def matchSimulatorSetup(teamOne, teamTwo):
    MATCH_ID = generateMATCH_ID()
    MATCH_ID = matchSimulator(MATCH_ID)
    createPlayingTeams(MATCH_ID, teamOne, teamTwo)
    return MATCH_ID


def simulateMatches(teamOne, teamTwo, n = 100):
    simulateCount = n
    MATCH_ID = matchSimulatorSetup(teamOne, teamTwo)

    for i in range(simulateCount):
        winner = startMatch(MATCH_ID, teamOne, teamTwo)
        if winner == teamOne:
            MATCH_ID.t1_wins +=1
        elif winner == teamTwo:
            MATCH_ID.t2_wins +=1
        else:
            MATCH_ID.ties +=1
        MATCH_ID.resetMatch()
    return MATCH_ID
    printSummary(MATCH_ID)

def printSummary(MATCH_ID):
    teamOne = MATCH_ID.battingOrder[0]
    teamTwo = MATCH_ID.battingOrder[1]
    print("{} won {} matches, {} won {} matches and {} matches were tied".format(teamOne, MATCH_ID.t1_wins, teamTwo, MATCH_ID.t2_wins, MATCH_ID.ties))

if __name__ == "__main__":
    blockPrint()
    theMatchID = simulateMatches(India, Pakistan)
    enablePrint()
    printSummary(theMatchID)
