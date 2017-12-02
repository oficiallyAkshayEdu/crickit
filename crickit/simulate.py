from crickit.Logger import *
from crickit.PlayCricket import *

__all__ = ['simulateMatches']

logger.setLevel('WARNING')


class matchSimulator():
    def __init__(self):
        self.t1_wins = 0
        self.t2_wins = 0
        self.ties = 0

        #TODO
        self.teamOne = []
        self.teamTwo = []
        self.teams = []
        self.matchCount = 0
        self.matches = []  #append all simulated matches here
        self.totalBallsBowled = 0
        self.totalOversBowled = 0
        self.totalWicketsTaken = 0
        # self.teamOne.meanRunScore = 0
        # self.teamOne.meanWicketsTaken = 0
        # OR self.teamOne.wicketsTaken.mean()

def simulateMatches(teamOne, teamTwo, simulateCount = 100):
    simulatedMatch = matchSimulator()
    for i in range(simulateCount):
        match = playMatch(teamOne, teamTwo)

        if match.winner == "draw":
            simulatedMatch.ties += 1
        elif match.winner.name == teamOne:
            simulatedMatch.t1_wins += 1
        elif match.winner.name == teamTwo:
            simulatedMatch.t2_wins += 1

        print("\rMatches Played.:{} | {} won: {} | {} won:{} | Matches Tied: {}".format(i + 1, teamOne,
                                                                                        simulatedMatch.t1_wins, teamTwo,
                                                                                        simulatedMatch.t2_wins,
                                                                                        simulatedMatch.ties),
              flush = True, end = '')
    return simulatedMatch


if __name__ == "__main__":

    simulatedaMatch = simulateMatches("India", "Pakistan", 10)
    print("\n")
    print(simulatedaMatch.t1_wins)