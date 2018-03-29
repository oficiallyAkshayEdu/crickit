class InningsA:
    def __init__(self, match, i):
        self.battingTeam = match.batting_order[i]
        self.bowlingTeam = match.bowling_order[i]
        self.delivery_count = 0
        self.over_counr = 0
        self.overs = list()
        self.deliveries = list()
        self.match = match
        self.innings_number = i
        # teamOne.resetBattingInnings()
        # teamOne.resetBowlingInnings()
        # teamTwo.resetBattingInnings()
        # teamTwo.resetBowlingInnings()
