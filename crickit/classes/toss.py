import random

from crickit.Logger import *


class Toss():
    def __init__(self, match):

        tosslog.info("Created Toss object")

        # private constants
        self.__COIN_FACES = ["Heads", "Tails"]

        # private
        self.__match = match
        self.__called_face = ""
        self.__called_by = []
        self.__face_up = []
        self.__face_down = []

        # public
        self.winner = []
        self.loser = []

        # exclude from Dict
        self.__EXCLUDES = [self.__match, self.__COIN_FACES]

        # fx call
        self.toss(self.__match)

    def toss(self, match):

        # tosses coin
        self.__face_up = random.choice(self.__COIN_FACES)
        self.__face_down = [x for x in self.__COIN_FACES if x != self.__face_up][0]

        self.__called_by = random.choice(match.playing_teams)
        self.__called_face = random.choice(self.__COIN_FACES)
        self.__called_by.toss_call = self.__called_face

        if self.__face_up == self.__called_face:
            self.winner = self.__called_by
            self.loser = [x for x in match.playing_teams if x != self.winner][0]
        else:
            self.loser = self.__called_by
            self.winner = [x for x in match.playing_teams if x != self.loser][0]
        tosslog.info(self.summary())
        # tosslog.info(self.debug())
        self.debug()

    def summary(self):
        return "{} called {} | Face up: {}  Face down: {} | {} wins,{} loses | ".format(self.__called_by, self.__called_face,
                                                                                        self.__face_up, self.__face_down,
                                                                                        self.winner, self.loser)

    # TODO fix this Repre
    def __repr__(self):
        return self.summary()

    def debug(self):
        for each in self.__dict__:
            # tosslog.debug(each)
            for excludes in self.__EXCLUDES:
                if self.__dict__[each] != excludes:
                    tosslog.debug("{}: {}".format(each, self.__dict__[each]))
                #     pass
        # return self.__dict__
        # all_attr = ""
        # for attr, value in self.__dict__.items():
        #     all_attr += "{}: {}".format(attr, value)
        # return all_attr
