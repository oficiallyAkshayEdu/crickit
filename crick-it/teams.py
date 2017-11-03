# from imports import *
from teamsList import *

# The Teams class
class Teams:
    #empty list to store all
    listTeams = []

    def addRuns(self, runs=1):
        self.runScore += runs

    def resetRuns(self):
        self.runScore = 0

    def plusInningsOverCount(self):
        # if self.overCount < 20:
        self.overCount +=1
        # else:
        #     self.overCount =20

    def resetBowlingInnings(self):
        self.overCount = 0
        self.resetBallCountPerOver()

    def resetBattingInnings(self):
        self.wicketCount = 0
        self.resetRuns()
        self.playedOvers = 0

    def boldOut(self):
        self.wicketCount +=1

    def plusBallCountPerOver(self):
        self.ballCountPerOver +=1

    def resetBallCountPerOver(self):
        self.ballCountPerOver = 0

    def __init__ (self, **entries):
        self.__dict__.update(entries)
        self.ballTypes = ['wideBall'] * int(self.wideBall*100) + ["noBall"]*(int(self.noBall*100)) + ['wicketBall']*int((self.wicketBall*100)) + ['regularBall']*int((self.regularBall*100))
        self.overCount = 0
        self.playCall = "Bat"
        Teams.listTeams.append(self)

    def __repr__(self):
        return self.name


India = Teams(**INDIA)
Pakistan = Teams(**PAKISTAN)