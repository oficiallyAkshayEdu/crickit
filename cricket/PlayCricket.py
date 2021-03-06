import operator
from decimal import Decimal

from cricket.classes import *
from cricket.teamsList import *

__all__ = ['play_match']


def play_match(t1, t2):
    matchlog.info("Match function triggered")
    match = Match()

    matchlog.debug("Team 1: {}  Team 2: {}".format(t1, t2))

    # matches passed team and instantiates it
    _instantiate_teams(t1, match)
    _instantiate_teams(t2, match)

    _start_match(match)

    # returns __match object to be stored as variable by calling function
    return match


def _start_match(match):
    # creates Toss object, stores it in the __match object
    match.toss = Toss(match)
    # loggProgress

    # creates playing order (batting and bowling order) within __match object
    match.create_batting_order()

    for i in range(2):
        match.innings_count = i
        _play_innings(match, i)

        declareMatchWinner(match)


def _instantiate_teams(team, match):
    '''
    :param team: (string) inputed by user/script of desired team
    :param match: current __match object
    :return: none
    # matches passedteam to list of teams in TEAMS_LIST and creates an instance of that team
    '''
    for each in TEAMS_LIST:
        if each['name'] == team:

            # creates Team object and passes unpacked team dict
            theTeam = Teams(**each)

            # appends team to the __match's playing_teams var
            match.playing_teams.append(theTeam)


def _play_innings(match, i):
    if i == 0:
        matchlog.debug("First Innings created")
        innings = InningsA(match, i)
        match.first_innings = innings
    elif i == 1:
        matchlog.debug("Second Innings created")
        innings = InningsA(match,i)
        match.second_innings = innings


    while innings.bowlingTeam.bowled_overs < match.OVER_COUNT:
        over(innings.battingTeam, innings.bowlingTeam, match)
        innings.bowlingTeam.plusInningsOverCount()


def batHit(battingTeam, bowlingTeam):
    # Function determines how many runs are scored off a ball which has been hit by the batsman

    batSkill = round(Decimal(random.uniform(0, battingTeam.bestBatSkill)), 3)
    bowlSkill = round(Decimal(random.uniform(0, bowlingTeam.maxBallDifficulty)), 3)

    # batSkill = battingTeam.bestBatSkill
    # bowlSkill = bowlingTeam.maxBallDifficulty
    if batSkill > bowlSkill:
        result = random.randint(1, 6)
        # todo detect if single, four or six
        return result

    elif batSkill == bowlSkill:
        result = random.randint(0, 4)
        # todo detect if dot, single, or four
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
    if match.innings_count == 1 and bowlingTeam.runs < battingTeam.runs:
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
        battingTeam.extras += 1

    isGameFinished(battingTeam, bowlingTeam, match)


def over(battingTeam, bowlingTeam, match):
    thisOver = Over()
    match.overs.append(thisOver)
    bowlingTeam.resetBallCountPerOver()
    while bowlingTeam.ballCountPerOver <= 5:
        delivery(battingTeam, bowlingTeam, thisOver, match)


def declareMatchWinner(match):
    """

    :param match: the current __match object
    :return: none
    """
    # calculates difference between the batting scores of both playing teams
    match.runs_delta = abs(match.playing_teams[0].runs - match.playing_teams[1].runs)

    # checks if __match was a tie and writes to __match object
    if match.runs_delta == 0:
        match.winner = "draw"

    else:
        winner = max(*match.playing_teams, key = operator.attrgetter('runs'))
        match.winner = winner
        match.loser = [x for x in match.playing_teams if x != match.winner][0]

    if __name__ == "__main__":
        match.match_summary()
