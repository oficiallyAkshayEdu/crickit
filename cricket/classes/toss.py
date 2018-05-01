import random

from cricket.Logger import *

tosslog.setLevel(logging.DEBUG)


class Toss:
    __slots__ = (
        '__COIN_FACES', '__match', 'called_face', 'called_by', 'face_up', 'face_down', 'winners_call', 'winner',
        'loser', '__logger')

    def __init__(self, match):

        tosslog.debug("Created Toss object")

        # private
        self.__logger = tosslog
        self.__COIN_FACES = ["Heads", "Tails"]
        self.__match = match

        # public
        self.winners_call = "" #winner chose to bat or bowl
        self.called_face = ""
        self.called_by = []
        self.face_up = []
        self.face_down = []
        self.winner = []
        self.loser = []

        # fx call
        self.toss(self.__match)


    def toss(self, match):

        self.winners_call = random.choice(("Bat", "Bowl"))

        # tosses coin
        self.face_up = random.choice(self.__COIN_FACES)
        self.face_down = [x for x in self.__COIN_FACES if x != self.face_up][0]

        self.called_by = random.choice(match.playing_teams)
        self.called_face = random.choice(self.__COIN_FACES)
        self.called_by.toss_call = self.called_face

        if self.face_up == self.called_face:
            self.winner = self.called_by
            self.loser = [x for x in match.playing_teams if x != self.winner][0]
        else:
            self.loser = self.called_by
            self.winner = [x for x in match.playing_teams if x != self.loser][0]
        # tosslog.info(self.summary())
        tosslog.info(self.__repr__())
        # print(self.__class__.__name__)
        debug(self, self.__class__.__name__)

    def __repr__(self):
        return "{} called {} | Face up: {}  Face down: {} | {} wins, {} loses | {} chooses to {} ".format(self.called_by,
                                                                                        self.called_face,
                                                                                        self.face_up,
                                                                                        self.face_down,
                                                                                        self.winner, self.loser, self.winner, self.winners_call)

    def debug(self, classname):
        for prop in self.__slots__:
            if prop.startswith("__"):
                prop = "_" + classname +prop
                self.__logger.debug("{}: {}".format(prop.title(), getattr(self, prop)))
            else:
                self.__logger.debug("Toss_{}: {}".format(prop.title(), getattr(self, prop)))

