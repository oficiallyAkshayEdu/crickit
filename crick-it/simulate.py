from playCricket import *

simulateCount = 100

def simulateXTimes():
    IndiaWinCount = 0
    PakistanWinCount = 0
    for i in range(simulateCount):
        winner = playCricket()
        if winner == India:
            IndiaWinCount +=1
        else:
            PakistanWinCount +=1
    print("\n")
    print("India won {}% matches, Pakistan won {}% Matches".format((IndiaWinCount*100)/simulateCount, (PakistanWinCount*100)/simulateCount))


if __name__ == "__main__":
    simulateXTimes()