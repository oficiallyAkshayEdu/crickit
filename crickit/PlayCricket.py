__all__ = ['playMatch']

import random

from crickit.Logger import *
from crickit.teamsList import *
from crickit.classes import *



logger.setLevel('DEBUG')

def start_match(match, teamOne, teamTwo):
    logger.info("match started between {} and {}".format(teamOne, teamTwo))
    coinToss(match)
    Innings(teamOne, teamTwo, match)
    Innings(teamTwo, teamOne, match)
    declareMatchWinner(match)
    # teamTwo.runScore = 0
    return match.winner


def generate_match_id():
    return str(uuid.uuid4())


def createPlayingTeams(MATCH_ID, teamOne, teamTwo):
    MATCH_ID.playingTeams.append(teamOne)
    MATCH_ID.playingTeams.append(teamTwo)


def instantTeam(*args):
    for team in TEAMS_LIST:
        for each in args:
            if team['name'] == each:
                theTeam = Teams(**team)
                return theTeam


def playMatch(teamOne, teamTwo):
    match = Match()

    teamOne = instantTeam(teamOne)
    match.teamOne = teamOne

    teamTwo = instantTeam(teamTwo)
    match.teamTwo = teamTwo

    createPlayingTeams(match, teamOne, teamTwo)
    start_match(match, teamOne, teamTwo)
    return match


def chooseMatchTeamsForTournament(match):
    # picks teams from the various defined teams
    match.playingTeams = random.sample(Teams.listTeams, 2)


def coinToss(match):
    match.toss = Toss()
    toss = match.toss
    toss.faceUp = random.choice(toss.coinFaces)
    toss.calledBy = random.choice(match.playingTeams)
    toss.calledFace = random.choice(toss.coinFaces)
    match.tempPlayingTeams = list(match.playingTeams)

    if toss.faceUp == toss.calledFace:
        toss.winner = toss.calledBy
        match.battingOrder.append(toss.calledBy)
        match.tempPlayingTeams.remove(toss.calledBy)
        match.battingOrder.append(match.tempPlayingTeams[0])
    else:
        match.tempPlayingTeams.remove(toss.calledBy)
        match.battingOrder.append(match.tempPlayingTeams[0])
        toss.winner = match.tempPlayingTeams[0]
        match.battingOrder.append(toss.calledBy)

    match.bowlingOrder = match.battingOrder[::-1]


def batHit(battingTeam, bowlingTeam):
    # Function determines how many runs are scored off a ball which has been hit by the batsman

    # batSkill = random.uniform(0, battingTeam.bestBatSkill)
    # bowlSkill = random.uniform(0, bowlingTeam.maxBallDifficulty)
    batSkill = battingTeam.bestBatSkill
    bowlSkill = bowlingTeam.maxBallDifficulty
    if batSkill > bowlSkill:
        result = random.randint(1, 6)
        # if result == 6:
        return result

    elif batSkill == bowlSkill:
        return random.randint(0, 4)
    else:
        battingTeam.boldOut()
        return 0
        # return random.randint(0,2)


def nextInning(battingTeam, bowlingTeam):
    bowlingTeam.ballCountPerOver = 6

    bowlingTeam.overCount = 21


def isGameFinished(battingTeam, bowlingTeam):
    if hasattr(bowlingTeam, 'runScore') and battingTeam.runScore > bowlingTeam.runScore:
        nextInning(battingTeam, bowlingTeam)
        # elif battingTeam.wicketCount == 9:
        #     nextInning(battingTeam, bowlingTeam)


def delivery(battingTeam, bowlingTeam, theOver, match):
    thisDelivery = Delivery()
    theOver.deliveries.append(thisDelivery)
    battingTeam.playedOvers = bowlingTeam.overCount

    ballTypes = ["regularBall", "wicketBall"]
    theBallType = random.choice(ballTypes)
    if theBallType == "regularBall":
        runs = batHit(battingTeam, bowlingTeam)
        # print(runs, "- ", end='', flush=True)
        battingTeam.addRuns(runs)
    elif theBallType == "wicketBall":
        # print("W", battingTeam.wicketCount, " - ", end='', flush=True)
        battingTeam.boldOut()
    isGameFinished(battingTeam, bowlingTeam)
    # elif theBallType =="wideBall":
    #     # print("I - ", end='', flush=True)
    #     battingTeam.addRuns()
    # elif theBallType =="noBall":
    #     # print("N - ", end='', flush=True)
    #     battingTeam.addRuns()


def over(battingTeam, bowlingTeam, match):
    thisOver = Over()
    match.overs.append(thisOver)
    bowlingTeam.resetBallCountPerOver()
    while bowlingTeam.ballCountPerOver <= 5:
        delivery(battingTeam, bowlingTeam, thisOver, match)
        bowlingTeam.plusBallCountPerOver()
    # logger.info(thisOver.deliveries[1])
    # print(match.overs, "\n")


def Innings(battingTeam, bowlingTeam, match):
    # sets teams runScore to 0
    battingTeam.resetBattingInnings()
    bowlingTeam.resetBowlingInnings()
    while bowlingTeam.overCount < match.OVER_COUNT:
        over(battingTeam, bowlingTeam, match)

        bowlingTeam.plusInningsOverCount()
        # print("{} played a total of {} overs, scored {} runs and lost {} wickets".format(battingTeam,
        # battingTeam.playedOvers, battingTeam.runScore, battingTeam.wicketCount))
    logger.info(len(match.overs))


import operator


def declareMatchWinner(match):
    """

    :param match: the current match object
    :return: none
    """
    # calculates difference between the batting scores of both placying teams
    match.runScoreDelta = abs(match.teamOne.runScore - match.teamTwo.runScore)

    # checks if match was a tie and writes to match object
    if match.runScoreDelta == 0:
        match.winner = "draw"
    else:
        winner = max(*match.playingTeams, key = operator.attrgetter('runScore'))
        match.winner = winner

    if __name__ == "__main__":
        match.matchSummary()

    return match.winner


#
if __name__ == "__main__":

    playMatch("India", "Pakistan")
