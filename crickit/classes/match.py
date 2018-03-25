from uuid import uuid4
from crickit.Logger import *
# uses UUID to generate unique match IDs

# declares inclusion of ONLY Match class to be imported
__all__ = ['Match']


class Match:
    def __init__(self):
        self.__match_ID = str(uuid4())

        # match sundries

        # match statistics
        self.playingTeams = list()
        self.winner = []
        self.loser = []
        self.toss = []

        self.overs = list()
        self.batting_order = []
        self.__bowling_order = []

        self.OVER_COUNT = 20
        self.runScoreDelta = 0  # todo
        self.wicketDelta = 0


    def createPlayingOrder(self):

        self.toss.winnerscall = random.choice(("bat", "bowl"))
        # debug(self.toss.winner)
        if winnerscall =="bat":
            self.batting_order.append(self.toss.winner)
            self.batting_order.append(self.toss.loser)
        else:
            self.batting_order.append(self.toss.loser)
            self.batting_order.append(self.toss.winner)

        # self.batting_order.append(self.toss.winner)
        # self.batting_order.append(self.toss.loser)
        # # find second team of batting order = first element of return list comprehension list
        # secondTeam = [x for x in self.playingTeams if x != self.toss.calledBy][0]
        # self.batting_order.append(secondTeam)
        # Reverse batting order to create the bowling order.
        self.__bowling_order = self.batting_order[::-1]

    # def __str__(self):
    #     summary = self.matchSummary()
    #     return summary

    def __repr__(self):
        all_attr = ""
        for attr, value in self.__dict__.items():
            all_attr += "{}: {} \n".format(attr, value)
        return all_attr

    def resetMatch(self):
        self.tossWinningTeam = []
        self.tossCallingTeam = []
        self.tossResult = []
        self.batting_order = []
        self.__bowling_order = []
        self.winningScore = 0
        self.winner = []
        self.loser = []
        self.winningTeamRuns = 0
        self.winningTeamWickets = 0
        self.losingTeamRuns = 0
        self.losingTeamWickets = 0
        self.runScoreDelta = 0
        self.wicketDelta = 0
        self.coinCalledByCallingTeam = ""

    # def matchSummary(self):
    #     return (
    #         "{} called {}, won the toss and decided to bat. {} won against {} by {} runs and {} wickets in {} "
    #         "overs".format(
    #                 self.toss.calledBy, self.toss.calledFace, self.winner, self.loser,
    #                 self.runScoreDelta, self.wicketDelta, "TOD"))

    def matchSummary(self):
        return ("{}: {} off {} balls and {} wickets \n {}: {} off {} balls and {} wickets \n {} won against {}".format(
            self.winner, self.winner.runs, "BALLS", "WICKETS", self.loser, self.losingTeamRuns, "BALLS",
            "WICKETS", self.winner, self.loser))
