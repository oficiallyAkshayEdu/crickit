# The Teams class
import random


class Teams:

    def __init__(self, **stats):

        # loads from dict
        self.__dict__.update(stats)

        # added vars
        self.ballCountPerOver = 0 #TODO
        self.wicketsLost = 0 #TODO
        self.playedOvers = 0 #TODO
        self.ballCountPerOver = 0 #TODO
        self.runs = 0
        self.bowled_overs = 0
        self.extras = 0

        self.ballTypes = ['wideBall'] * self.wideBall + ["noBall"] * self.noBall + ['regularBall'] * self.regularBall
        random.shuffle(self.ballTypes)

    def resetTeam(self):
        self.runs = 0
        self.bowled_overs = 0
        self.ballCountPerOver = 0 #todo Outide scope declaration

    def addRuns(self, added_runs = 1):
        self.runs += added_runs

    def resetRuns(self):
        self.runs = 0

    def plusInningsOverCount(self):
        # if self.bowled_overs < 20:
        self.bowled_overs += 1
        # else:
        #     self.bowled_overs =20

    def resetBowlingInnings(self):
        self.bowled_overs = 0
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
