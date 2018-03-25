# The Teams class
import random


class Teams:

    def __init__(self, **stats):
        self.overCount = 0
        self.__dict__.update(stats)
        # self.runScore = 0
        self.ballTypes = ['wideBall'] * self.wideBall + ["noBall"] * self.noBall+ ['wicketBall'] \
                           * self.wicketBall+ ['regularBall'] * self.regularBall
        # random.shuffle(self.ballTypes)



    def resetTeam(self):
        self.runScore = 0
        self.overCount = 0
        self.ballCountPerOver = 0

    def addRuns(self, runs=1):
        self.runScore += runs

    def resetRuns(self):
        self.runScore = 0

    def plusInningsOverCount(self):
        # if self.overCount < 20:
        self.overCount += 1
        # else:
        #     self.overCount =20

    def resetBowlingInnings(self):
        self.overCount = 0
        self.resetBallCountPerOver()

    def resetBattingInnings(self):
        self.wicketsLost = 0
        self.resetRuns()
        self.playedOvers = 0

    def boldOut(self):
        self.wicketsLost += 1

    def plusBallCountPerOver(self):
        self.ballCountPerOver += 1

    def resetBallCountPerOver(self):
        self.ballCountPerOver = 0

    def __repr__(self):
        if __name__ == '__main__':
            # return self.name
            all_attr = ""
            for attr, value in self.__dict__.items():
                all_attr += "{}: {} \n".format(attr, value)
            return all_attr
        else:
            return self.name
