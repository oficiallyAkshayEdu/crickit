from uuid import uuid4

class Match:
    def __init__(self):
        self.match_ID = str(uuid4())
        # match sundries
        self.battingOrder = []
        self.bowlingOrder = []
        self.OVER_COUNT = 20
        self.overs = list()

        # match statistics
        self.loser = []
        self.losingTeamRuns = 0
        self.losingTeamWickets = 0
        self.playingTeams = []
        self.runScoreDelta = 0
        self.winner = []
        self.winningScore = 0
        self.wicketDelta = 0
        # self.winningTeamRuns = 0
        # self.winningTeamWickets = 0



    def __repr__(self):
        return self.matchID

    def resetMatch(self):
        self.tossWinningTeam = []
        self.tossCallingTeam = []
        self.tossResult = []
        self.battingOrder = []
        self.bowlingOrder = []
        self.winningScore = 0
        self.winner = []
        self.loser = []
        self.winningTeamRuns = 0
        self.winningTeamWickets = 0
        self.losingTeamRuns = 0
        self.losingTeamWickets = 0
        self.runScoreDelta = 0
        self.wicketDelta = 0
        self.coinCalledByCallingTeam = ""

    def matchSummary(self):
        print(
                "{} called {}, won the toss and decided to bat. {} won against {} by {} runs and {} wickets in {} "
                "overs".format(
                        self.toss.calledBy, self.toss.calledFace, self.winner, self.loser,
                        self.runScoreDelta, self.wicketDelta, "TODO"))
