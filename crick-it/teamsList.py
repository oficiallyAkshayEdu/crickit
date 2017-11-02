from teams import *

################## Define all the teams and their characteristics ##################
India = Teams("India", "Heads",0.3,0.35, 0.2, 0.5, 0.85, 0.65)

Pakistan = Teams("Pakistan", "Tails",0.2, 0.45, 0.1,0.8, 0.75, 0.45)

# Australia = Teams("Australia", "Heads", "Bowl", 1,1)

# England = Teams("England", "Heads", "Bowl", 0,0)

# Zimbabwe = Teams("Zimbabwe", 0.9, "Heads", "Bowl", 0.06)


India22 = {
    'name': "India2",
    'tossCall': "Heads",
    'noBall': 0.3,
    'wideBall': 0.35,
    'wicketBall': 0.2,
    'regularBall': 0.5,
    'maxBallDifficulty':0.85,
    'bestBatSkill': 0.65
}

class testTeams:

    def __init__ (self, **entries):
        self.__dict__.update(entries)
    def __repr__(self):
        return self.name

India32 = testTeams(**India22)

India32
print(India32.bestBatSkill)

