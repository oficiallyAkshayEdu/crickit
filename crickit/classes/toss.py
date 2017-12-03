import random


class Toss():
    def __init__(self, match):
        self.coinFaces = ["Heads", "Tails"]
        self.calledFace = ""
        self.calledBy = []
        self.winner = []
        self.loser = []
        self.faceUp = []
        self.faceDown = []
        self.match = match
        self.toss()

    def theOtherTeam(self, firstTeam):
        otherTeam = (filter(lambda x: x != firstTeam, self.match.playingTeams))
        otherTeam = ', '.join(str(x) for x in otherTeam)  # converts filter object to printable team name for __repr__
        return otherTeam

    def toss(self):
        match = self.match
        self.faceUp = random.choice(self.coinFaces)
        self.faceDown = ''.join(list(filter(lambda x: x != self.faceUp, self.coinFaces)))  # ensures output is a string
        self.calledBy = random.choice(match.playingTeams)
        self.calledFace = random.choice(self.coinFaces)

        if self.faceUp == self.calledFace:
            self.winner = self.calledBy
            self.loser = self.theOtherTeam(self.winner)
        else:
            self.loser = self.calledBy
            self.winner = self.theOtherTeam(self.loser)

    def __repr__(self):
        return "{} called {}. Coin landed {} face up. {} won the toss and decided to bat".format(
                self.calledBy, self.calledFace, self.faceUp, self.winner
                )
