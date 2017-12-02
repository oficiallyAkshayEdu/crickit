# The Teams class
class Teams:
    def __init__(self, **stats):
        self.__dict__.update(stats)
        self.ballTypes = ['wideBall'] * self.wideBall * 100 + ["noBall"] * self.noBall * 100 + ['wicketBall'] \
                           * self.wicketBall * 100 + ['regularBall'] * (self.regularBall *100)
        self.overCount = 0


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
        self.wicketCount = 0
        self.resetRuns()
        self.playedOvers = 0

    def boldOut(self):
        self.wicketCount += 1

    def plusBallCountPerOver(self):
        self.ballCountPerOver += 1

    def resetBallCountPerOver(self):
        self.ballCountPerOver = 0

    def __repr__(self):
        return self.name




        # India = Teams(**INDIA)
        # Pakistan = Teams(**PAKISTAN)
        # Zimbabwe = Teams(**ZIMBABWE)
