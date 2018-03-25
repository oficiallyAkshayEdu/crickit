import random

from crickit.Logger import *


class Toss():
    def __init__(self, match):
        tosslog.info("Created Toss object")
        self.__COIN_FACES = ["Heads", "Tails"]
        self.calledFace = ""
        self.calledBy = []
        self.winner = []
        self.loser = []
        self.faceUp = []
        self.faceDown = []
        self.match = match
        self.toss()

    def toss(self):

        # shorten self.match to refer to this toss' match teams and data easily
        match = self.match

        # tosses coin
        self.faceUp = random.choice(self.__COIN_FACES)
        self.faceDown = [x for x in self.__COIN_FACES if x != self.faceUp][0]
        self.calledBy = random.choice(match.playingTeams)
        self.calledFace = random.choice(self.__COIN_FACES)
        self.calledBy.toss_call = self.calledFace

        if self.faceUp == self.calledFace:
            self.winner = self.calledBy
            self.loser = [x for x in match.playingTeams if x != self.winner][0]
            # self.loser = self.theOtherTeam(self.winner)
        else:
            self.loser = self.calledBy
            self.winner = [x for x in match.playingTeams if x != self.loser][0]
            # self.winner = self.theOtherTeam(self.loser)
        tosslog.info(self.summary())

    def summary(self):
        return "{} called {} | Face up: {}  Face down: {} | {} wins,{} loses | ".format(self.calledBy, self.calledFace,
                                                                                        self.faceUp, self.faceDown,
                                                                                        self.winner, self.loser)

    # TODO fix this Repre
    def __repr__(self):
        return self.summary()
