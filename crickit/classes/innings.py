class InningsA:
    def __init__(self, teamOne, teamTwo, i, match):
        self.battingTeam = []
        self.bowlingTeam = []
        self.delivery_count = 0
        self.over_counr = 0
        self.overs = list()
        self.deliveries = list()
        self.match = match
        self.innings_number = i
        teamOne.resetBattingInnings()
        teamOne.resetBowlingInnings()
        teamTwo.resetBattingInnings()
        teamTwo.resetBowlingInnings()
