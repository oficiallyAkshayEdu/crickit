'''
This file defines all the teams in play. For current version the game is simulated only between two teams - India and Pakistan
'''

INDIA = {
    'name': "India",
    'tossCall': "Heads",
    'noBall': 0.20,
    'wideBall': 0.05,
    'wicketBall': 0.05,
    'regularBall': 0.70,
    'maxBallDifficulty':0.75,
    'bestBatSkill': 0.85
}


PAKISTAN = {
    'name': "Pakistan",
    'tossCall': "Tails",
    'noBall': 0.15,
    'wideBall': 0.05,
    'wicketBall': 0.05,
    'regularBall': 0.65,
    'maxBallDifficulty':0.85,
    'bestBatSkill': 0.65
}