import random

from crickit.Logger import *


class Toss:

    # todo figure out slots
    # __slots__ = ('__dict__','__COIN_FACES','__match', '__called_face', '__called_by', '__face_up', '__face_down',
    # '_winners_call', 'winner','loser')
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

        # protected
        self._winners_call = ""

        # public
        self.winner = []
        self.loser = []
        tosslog.info(self.__dict__)
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
        self.debug()

    def summary(self):
        return "{} called {} | Face up: {}  Face down: {} | {} wins,{} loses | ".format(self.__called_by,
                                                                                        self.__called_face,
                                                                                        self.__face_up,
                                                                                        self.__face_down,
                                                                                        self.winner, self.loser)

    def __repr__(self):
        return self.summary()

    def debug(self):
        for each in self.__dict__:
            tosslog.debug("{}: {}".format(each, self.__dict__[each]))
