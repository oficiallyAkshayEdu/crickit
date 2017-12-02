'''
This file defines all the teams in play. For current version the game is simulated only between two teams - India and Pakistan
'''

INDIA = {
    'name': "India",
    'tossCall': "Heads",
    'noBall': 10,
    'wideBall': 5,
    'wicketBall': 5,
    'regularBall': 65,
    'maxBallDifficulty': 0.75,
    'bestBatSkill': 0.95
}


PAKISTAN = {
    'name': "Pakistan",
    'tossCall': "Tails",
    'noBall': 10,
    'wideBall': 5,
    'wicketBall': 5,
    'regularBall': 65,
    'maxBallDifficulty': 0.75,
    'bestBatSkill': 0.95
}

ZIMBABWE = {
    'name': "Zimbabwe",
    'tossCall': "Tails",
    'noBall': 15,
    'wideBall': 5,
    'wicketBall': 5,
    'regularBall': 65,
    'maxBallDifficulty': 0.85,
    'bestBatSkill': 0.65
}

TEAMS_LIST = [ZIMBABWE, INDIA, PAKISTAN]