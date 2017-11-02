# from imports import *

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

    def __init__ (self, name, tossCall, noBall, wideBall,wicketBall, regularBall, maxBallDifficulty,bestBatSkill):
        self.tossCall = tossCall
        self.playCall = "Bat"
        self.name = name
        self.noBall = noBall
        self.wideball = wideBall
        self.wicketBall = wicketBall
        self.regularBall = regularBall
        self.maxBallDifficulty = maxBallDifficulty
        self.bestBatSkill = bestBatSkill

        self.ballTypes = ['wideBall'] * int(wideBall*100) + ["noBall"]*(int(noBall*100)) + ['wicketBall']*int((wicketBall*100)) + ['regularBall']*int((regularBall*100))
        self.overCount = 0
        Teams.listTeams.append(self)

    def __repr__(self):
        return self.name
