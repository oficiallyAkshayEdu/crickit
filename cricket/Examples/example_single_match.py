matchlog.info("Started Example Script. Importing cricket next")
import cricket
matchlog.info("cricket Imported Successfully")


match = cricket.play_match("India", "Pakistan")


# simulatedMatch = cricket.simulateMatches("India","Pakistan", 10)
# print(__match.loser.runs, __match.loser)
# print(__match.winner.runs, __match.winner)
print()
# print(__match.__repr__)
print(match.loser.wicketsLost, match.winner.wicketsLost)
print(match.winner.runs, match.winner)
print(match.loser.runs, match.loser)
# print(len(cricket.Teams.allteamobjects))
# print(simulatedMatch.matches[1].winner.runs)
# print(simulatedMatch.matches[2].winner.runs)
# print(simulatedMatch.matches[3].winner.runs)