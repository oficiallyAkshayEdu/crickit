# imports all imports from the import file
from imports import *

coinFaces = ["Heads", "Tails"]

# A T20 Match has 20 overs
OVER_COUNT = 20
'''
Picks playing teams, creates team player list, does the coin toss which determines playing order.
Pl note this is a futuristic feature - this will probably be used in the future when Crickit develops
into a multi-team multi-player tournament simulator
'''


def setup():
    # picks teams from the various defined teams
    pickedTeams = teamPicker()
    
    # saves the returned batting order
    battingOrderTeams = coinToss(pickedTeams)
    return battingOrderTeams

def teamPicker():
    #randomly picks two teams from the list of all the teams
    playingTeams = random.sample(Teams.listTeams, 2)
    return playingTeams

def coinToss(thePickedTeams):
    # Initilizations
    tossWinningTeam = []
    battingOrderTeams = []

    # Assignments
    callingTeam = random.choice(thePickedTeams)
    tossresult = random.choice(coinFaces)

    # print Block
    print("The coin is tossed...")
    print(callingTeam, "calls", callingTeam.tossCall)
    print("The coin lands with", tossresult, "face up")

    # Creates the order the teams will bat - the "batting order"
    for i in range(len(thePickedTeams)):
        if tossresult == thePickedTeams[i].tossCall:
            tossWinningTeam = thePickedTeams[i]
            battingOrderTeams.append(thePickedTeams[i])

            #assigns the team other than the winning team as the SECOND batting team

            if i == 1:
                j = 0
                battingOrderTeams.append(thePickedTeams[j])
            else:
                j = 1
                battingOrderTeams.append(thePickedTeams[j])

    print(tossWinningTeam, "wins and decides to", tossWinningTeam.playCall, "first")
    return battingOrderTeams


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

    # todo add delivery function here
    # todo check if game has been won

    while bowlingTeam.ballCountPerOver <= 5:
        delivery(battingTeam, bowlingTeam)
        bowlingTeam.plusBallCountPerOver()

        # time.sleep(0.5)



def Innings(battingTeam, bowlingTeam):

    # sets teams runScore to 0
    battingTeam.resetBattingInnings()
    bowlingTeam.resetBowlingInnings()
    while bowlingTeam.overCount < OVER_COUNT:
        over(battingTeam, bowlingTeam)
        # print("")
        bowlingTeam.plusInningsOverCount()
    print("{} played a total of {} overs, scored {} runs and lost {} wickets".format(battingTeam, battingTeam.playedOvers, battingTeam.runScore, battingTeam.wicketCount))
    # print(battingTeam, "scored a total of", battingTeam.runScore, "runs at ", battingTeam.wicketCount, "wickets")


def declareWinner(teams):
    winningTeam = []
    highestScore = 0

    differenceInScore = abs(teams[0].runScore - teams[1].runScore)


    differenceInWickets = abs(teams[0].wicketCount - teams[1].wicketCount)
    for team in teams:
        if team.runScore > highestScore:
            highestScore = team.runScore
            winningTeam = team

    if teams[0].wicketCount > teams[1].wicketCount:
        print("{} wins by {} wickets".format(winningTeam, differenceInWickets))
    elif teams[0].runScore == teams[1].runScore:
        print("The game is tied!")
        winningTeam = "None"
    else:
        print("{} wins by {} runs".format(winningTeam, differenceInScore))

    return winningTeam


# sets up game and passes each playing team as argument to Innings
def playCricket():
    battingOrderTeams = setup()
    bowlingOrderTeams = battingOrderTeams[::-1]
    for i in range(2):
        Innings(battingOrderTeams[i], bowlingOrderTeams[i])
    theWinner = declareWinner(battingOrderTeams)
    return theWinner



if __name__ == "__main__":
    # print("hello")
    playCricket()
# elif __name__ == "simulate":
#     print("hello there")

#TODO stretch goals
# todo if no runs - decalre and print - maiden
