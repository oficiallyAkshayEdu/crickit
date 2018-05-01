import random

from cricket.Logger import *

# declares inclusion of ONLY Match class to be imported
__all__ = ['Match']

matchlog.setLevel(logging.DEBUG)


class Match:
    def __init__(self):

        self.OVER_COUNT = 20

        # object stores
        self.toss = []
        self.overs = list()  # list of all over objects

        self.playing_teams = list()

        self.batting_order = []
        self.bowling_order = []

        self.winner = []
        self.loser = []

        # added vars
        self.winning_score = 0  # TODO
        self.runs_delta = 0  # TODO
        self.wickets_delta = 0  # TODO
        self.innings_count = 0
        self.first_innings = []
        self.second_innings = []

        # balling stats
        self.balls_thrown = 0  # TODO
        self.extras = 0  # TODO
        self.singles = 0  # TODO
        self.dot_balls = 0  # TODO
        self.sixes = 0  # TODO
        self.fours = 0  # TODO
        self.over_count = len(self.overs)  # TODO

    def create_batting_order(self):



        if self.toss.winners_call == "Bat":
            self.batting_order.append(self.toss.winner)
            self.batting_order.append(self.toss.loser)
        elif self.toss.winners_call == "Bowl":
            self.batting_order.append(self.toss.loser)
            self.batting_order.append(self.toss.winner)

        # bowling order = reverse of batting order
        self.bowling_order = self.batting_order[::-1]

        matchlog.info(
                "{} wins the toss, decides to {}".format(self.toss.winner.name.upper(),
                                                         (self.toss.winners_call.upper())))
        matchlog.info("Batting order: {}".format(self.batting_order))
        matchlog.info("Bowling order: {}".format(self.bowling_order))

    # def match_summary(self):
    #     return (
    #         "{} called {}, won the toss and decided to bat. {} won against {} by {} runs and {} wickets in {} "
    #         "overs".format(
    #                 self.toss.called_by, self.toss.called_face, self.winner, self.loser,
    #                 self.runs_delta, self.wickets_delta, "TOD"))

    def match_summary(self):
        return ("{}: {} off {} balls and {} wickets \n {}: {} off {} balls and {} wickets \n {} won against {}".format(
                self.winner, self.winner.runs, "BALLS", "WICKETS", self.loser, self.losingTeamRuns, "BALLS",
                "WICKETS", self.winner, self.loser))
