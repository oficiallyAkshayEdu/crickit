import operator

from crickit.Logger import *
from crickit.classes import *
from crickit.teamsList import *
from decimal import Decimal
import logging



__all__ = ['play_match']


def play_match(t1, t2):
    matchlog.info("Match function triggered")
    match = Match()


    matchlog.debug("Team 1: {}  Team 2: {}".format(t1, t2))

    # matches passed team and instantiates it
    _instantiate_teams(t1, match)
    _instantiate_teams(t2, match)

    _start_match(match)

    #returns match object to be stored as variable by calling function
    return match

def _start_match(match):

    # creates Toss object, stores it in the match object
    match.toss = Toss(match)

    match.create_batting_order()  # creates playing order (batting and bowling order) within match object


    for i in range(2):
        match._inningsCount = i
        Innings(match, i)

        declareMatchWinner(match)


# def createPlayingTeams(match, teamOne, teamTwo):
#     match.playingTeams.append(teamOne)
#     match.playingTeams.append(teamTwo)


def _instantiate_teams(team, match):
    '''
    :param team: (string) inputed by user/script of desired team
    :param match: current match object
    :return: none
    # matches passedteam to list of teams in TEAMS_LIST and creates an instance of that team
    '''
    for each in TEAMS_LIST:
        if each['name'] == team:
            theTeam = Teams(**each)
            match.playingTeams.append(theTeam)

def Innings(match, i):
    # sets teams runs to 0
    battingTeam = match.batting_order[i]
    bowlingTeam = match.bowling_order[i]
    battingTeam.resetBattingInnings()
    bowlingTeam.resetBowlingInnings()
    while bowlingTeam.bowled_overs < match.OVER_COUNT:
        over(battingTeam, bowlingTeam, match)
        bowlingTeam.plusInningsOverCount()

# todo make coinToss accesible via API
# def coinToss(match):
#     match.toss = Toss()
#     toss = match.toss
#     toss.faceUp = random.choice(toss.__COIN_FACES)
#     toss.calledBy = random.choice(match.playingTeams)
#     toss.calledFace = random.choice(toss.__COIN_FACES)
#     match.tempPlayingTeams = list(match.playingTeams)
#
#     if toss.faceUp == toss.calledFace:
#         toss.winner = toss.calledBy
#         match.battingOrder.append(toss.calledBy)
#         match.tempPlayingTeams.remove(toss.calledBy)
#         match.battingOrder.append(match.tempPlayingTeams[0])
#     else:
#         match.tempPlayingTeams.remove(toss.calledBy)
#         match.battingOrder.append(match.tempPlayingTeams[0])
#         toss.winner = match.tempPlayingTeams[0]
#         match.battingOrder.append(toss.calledBy)
#
#     match.bowlingOrder = match.battingOrder[::-1]


def batHit(battingTeam, bowlingTeam):
    # Function determines how many runs are scored off a ball which has been hit by the batsman

    batSkill = round(Decimal(random.uniform(0, battingTeam.bestBatSkill)),3)
    bowlSkill = round(Decimal(random.uniform(0, bowlingTeam.maxBallDifficulty)),3)

    # batSkill = battingTeam.bestBatSkill
    # bowlSkill = bowlingTeam.maxBallDifficulty
    if batSkill > bowlSkill:
        result = random.randint(1, 6)
        #todo detect if single, four or six
        return result

    elif batSkill == bowlSkill:
        result = random.randint(0,4)
        #todo detect if dot, single, or four
        return result
    elif batSkill < bowlSkill:
        battingTeam.boldOut()
        return 0


def nextInning(battingTeam, bowlingTeam):
    bowlingTeam.ballCountPerOver = 6
    bowlingTeam.bowled_overs = 21


def isGameFinished(battingTeam, bowlingTeam, match):
    if battingTeam.wicketsLost == 9:
        nextInning(battingTeam, bowlingTeam)
    if match._inningsCount == 1 and bowlingTeam.runs < battingTeam.runs:
        nextInning(battingTeam, bowlingTeam)

def delivery(battingTeam, bowlingTeam, theOver, match):
    thisDelivery = Delivery()
    theOver.deliveries.append(thisDelivery)
    battingTeam.playedOvers = bowlingTeam.bowled_overs


    ballTypes = ["regularBall", "noBall", "wideBall"]
    theBallType = random.choice(ballTypes)
    if theBallType == "regularBall":
        runs = batHit(battingTeam, bowlingTeam)

        battingTeam.addRuns(runs)
        bowlingTeam.plusBallCountPerOver()
    elif theBallType == "noBall" or theBallType == "wideBall":
        battingTeam.addRuns()
        battingTeam.extras +=1

    isGameFinished(battingTeam, bowlingTeam, match)



def over(battingTeam, bowlingTeam, match):
    thisOver = Over()
    match.overs.append(thisOver)
    bowlingTeam.resetBallCountPerOver()
    while bowlingTeam.ballCountPerOver <= 5:
        delivery(battingTeam, bowlingTeam, thisOver, match)

def declareMatchWinner(match):
    """

    :param match: the current match object
    :return: none
    """
    # calculates difference between the batting scores of both playing teams
    match.runScoreDelta = abs(match.playingTeams[0].runs - match.playingTeams[1].runs)

    # checks if match was a tie and writes to match object
    if match.runScoreDelta == 0:
        match.winner = "draw"

    else:
        winner = max(*match.playingTeams, key = operator.attrgetter('runs'))
        match.winner = winner
        match.loser = [x for x in match.playingTeams if x!= match.winner][0]


    if __name__ == "__main__":
        match.matchSummary()

