from crickit.Logger import *
from crickit.PlayCricket import *

__all__ = ['simulateMatches']

# matchlog.setLevel('WARNING')


class matchSimulator():

    def __init__(self):
        self.t1_wins = 0
        self.t2_wins = 0
        self.ties = 0
        self.matches = list()

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

    def __repr__(self):
        all_attr = ""
        for attr, value in self.__dict__.items():
            all_attr += "{}: {} \n".format(attr, value)
        return all_attr

def simulateMatches(teamOne, teamTwo, simulateCount = 100):
    simulatedMatch = matchSimulator()
    for i in range(simulateCount):
        match = play_match(teamOne, teamTwo)
        simulatedMatch.matches.append(match)

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
