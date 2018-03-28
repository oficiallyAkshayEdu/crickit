from uuid import uuid4
from crickit.Logger import *
import random
# uses UUID to generate unique __match IDs

# declares inclusion of ONLY Match class to be imported
__all__ = ['Match']


class Match:
    def __init__(self):
        self.__match_ID = str(uuid4())
        self.OVER_COUNT = 20

        # object stores
        self.toss = []
        self.overs = list() # list of all over objects

        self.playing_teams = list()

        self.batting_order = []
        self.bowling_order = []

        self.winner = []
        self.loser = []

        self.runScoreDelta = 0  # todo
        self.wicketDelta = 0 #todo


    def create_batting_order(self):

        self.toss.winnerscall = random.choice(("bat", "bowl"))
        matchlog.info("{} wins the toss, decides to {}".format(self.toss.winner.name.upper(), (self.toss.winnerscall.upper())))
        if self.toss.winnerscall =="bat":
            self.batting_order.append(self.toss.winner)
            self.batting_order.append(self.toss.loser)
        elif self.toss.winnerscall == "bowl":
            self.batting_order.append(self.toss.loser)
            self.batting_order.append(self.toss.winner)
        else:
            error("winnerscall {} out of expected outcome".format(self.toss.winnerscall))

        self.bowling_order = self.batting_order[::-1]
        matchlog.info("Batting order: {}".format(self.batting_order))
        matchlog.info("Bowling order: {}".format(self.bowling_order))

    # def __str__(self):
    #     summary = self.matchSummary()
    #     return summary

    def __repr__(self):
        return self.__match_ID
    #     all_attr = ""
    #     for attr, value in self.__dict__.items():
    #         all_attr += "{}: {} \n".format(attr, value)
    #     return all_attr

    def resetMatch(self):
        self.tossWinningTeam = []
        self.tossCallingTeam = []
        self.tossResult = []
        self.batting_order = []
        self.bowling_order = []
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
    #                 self.toss.__called_by, self.toss.__called_face, self.winner, self.loser,
    #                 self.runScoreDelta, self.wicketDelta, "TOD"))

    def matchSummary(self):
        return ("{}: {} off {} balls and {} wickets \n {}: {} off {} balls and {} wickets \n {} won against {}".format(
            self.winner, self.winner.runs, "BALLS", "WICKETS", self.loser, self.losingTeamRuns, "BALLS",
            "WICKETS", self.winner, self.loser))
