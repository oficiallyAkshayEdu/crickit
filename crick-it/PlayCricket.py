# imports all imports from the import file
from imports import *

coinFaces = ["Heads", "Tails"]

# A T20 Match has 20 overs
OVER_COUNT = 20
NUM_MATCHES = 1


def startMatch(matchID,teamOne,teamTwo):
    coinToss(matchID)
    Innings(teamOne, teamTwo)
    Innings(teamTwo, teamOne)
    declareMatchWinner(matchID)
    return matchID.InningsWinner

def generateMATCH_ID():
    MATCH_ID = str(uuid.uuid4())
    return MATCH_ID

def createPlayingTeams(MATCH_ID, teamOne, teamTwo):
    MATCH_ID.playingTeams.append(teamOne)
    MATCH_ID.playingTeams.append(teamTwo)
    print(MATCH_ID.playingTeams)

def playMatch(teamOne, teamTwo):
    MATCH_ID = generateMATCH_ID()
    MATCH_ID = Match(MATCH_ID)
    createPlayingTeams(MATCH_ID, teamOne, teamTwo)
    startMatch(MATCH_ID, teamOne, teamTwo)
    return MATCH_ID.InningsWinner

def chooseMatchTeamsForTournament(match):
    # picks teams from the various defined teams
    match.playingTeams = random.sample(Teams.listTeams, 2)

def coinToss(match):
    match.tossResult = random.choice(coinFaces)
    match.callingTeam = random.choice(match.playingTeams)
    match.coinCalledByCallingTeam = random.choice(coinFaces)
    TheCallingTeam = match.callingTeam
    TheTossResult = match.tossResult

    # print Block
    match.tempPlayingTeams = list(match.playingTeams)

    if TheTossResult == match.coinCalledByCallingTeam:
        match.tossWinningTeam = match.callingTeam
        match.battingOrder.append(match.callingTeam)
        match.tempPlayingTeams.remove(match.callingTeam)
        match.battingOrder.append(match.tempPlayingTeams[0])
    else:
        match.tempPlayingTeams.remove(match.callingTeam)
        match.battingOrder.append(match.tempPlayingTeams[0])
        match.tossWinningTeam = match.tempPlayingTeams[0]
        match.battingOrder.append(match.callingTeam)


    match.bowlingOrder = match.battingOrder[::-1]
    TheTossWinningTeam = match.tossWinningTeam


def batHit(battingTeam, bowlingTeam):
    # FUnction determines how many runs are scored off a ball which has been hit by the batsman

    batSkill = random.uniform(0, battingTeam.bestBatSkill)
    bowlSkill = random.uniform(0, bowlingTeam.maxBallDifficulty)
    if batSkill > bowlSkill:
        result = random.randint(1,6)
        # if result == 6:
        return result

    elif batSkill == bowlSkill:
        return random.randint(0,4)
    else:
        return random.randint(0,2)

def nextInning(battingTeam, bowlingTeam):
    bowlingTeam.ballCountPerOver = 6

    bowlingTeam.overCount = 21

def isGameFinished(battingTeam, bowlingTeam):
    if hasattr(bowlingTeam, 'runScore') and battingTeam.runScore > bowlingTeam.runScore:
        nextInning(battingTeam, bowlingTeam)
    elif battingTeam.wicketCount == 9:
        nextInning(battingTeam, bowlingTeam)

def delivery(battingTeam, bowlingTeam):
    battingTeam.playedOvers = bowlingTeam.overCount
    isGameFinished(battingTeam, bowlingTeam)
    theBallType = random.choice(bowlingTeam.ballTypes)
    if theBallType == "regularBall":
        runs = batHit(battingTeam, bowlingTeam)
        # print(runs, "- ", end='', flush=True)
        battingTeam.addRuns(runs)
    elif theBallType =="wicketBall":
        # print("W", battingTeam.wicketCount, " - ", end='', flush=True)
        battingTeam.boldOut()
    elif theBallType =="wideBall":
        # print("I - ", end='', flush=True)
        battingTeam.addRuns()
    elif theBallType =="noBall":
        # print("N - ", end='', flush=True)
        battingTeam.addRuns()


def over(battingTeam, bowlingTeam):
    bowlingTeam.resetBallCountPerOver()
    while bowlingTeam.ballCountPerOver <= 5:
        delivery(battingTeam, bowlingTeam)
        bowlingTeam.plusBallCountPerOver()

def Innings(battingTeam, bowlingTeam):

    # sets teams runScore to 0
    battingTeam.resetBattingInnings()
    bowlingTeam.resetBowlingInnings()
    while bowlingTeam.overCount < OVER_COUNT:
        over(battingTeam, bowlingTeam)

        bowlingTeam.plusInningsOverCount()
    # print("{} played a total of {} overs, scored {} runs and lost {} wickets".format(battingTeam, battingTeam.playedOvers, battingTeam.runScore, battingTeam.wicketCount))

def declareMatchWinner(match):

    match.runScoreDelta = abs(match.battingOrder[0].runScore - match.battingOrder[1].runScore)
    match.wicketDelta = abs(match.battingOrder[0].wicketCount - match.battingOrder[1].wicketCount)
    for team in match.playingTeams:
        if team.runScore > match.winningScore:
            match.winningScore = team.runScore
            match.InningsWinner = team

    #todo account for tie condition

    match.matchSummary()


if __name__ == "__main__":
    playMatch(India, Pakistan)

#TODO stretch goals
# todo if no runs - decalre and print - maiden
