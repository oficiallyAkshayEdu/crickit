from cricket.Logger import *

class InningsA:
    def __init__(self, match, i):
        self.match = match
        self.innings_number = i


        self.battingTeam = match.batting_order[i]
        self.bowlingTeam = match.bowling_order[i]


        inningslog.info("Innings Number: {}. {} is bating, {} is bowling".format(self.innings_number, self.battingTeam, self.bowlingTeam))

        # balling stats
        self.overs = list()
        self.balls_thrown = 0 #TODO
        self.extras = 0 #TODO
        self.singles = 0 #TODO
        self.dot_balls = 0 #TODO
        self.sixes = 0 #TODO
        self.fours = 0 #TODO
        self.over_count = len(self.overs) #TODO


        # self.deliveries = list()
    def __repr__(self):
        return self.innings_number

