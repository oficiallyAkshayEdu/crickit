matchlog.info("Started Example Script. Importing Crickit next")
import crickit
matchlog.info("Crickit Imported Successfully")


match = crickit.play_match("India", "Pakistan")

# simulatedMatch = crickit.simulateMatches("India","Pakistan", 10)

# print(match.loser.runs, match.loser)
# print(match.winner.runs, match.winner)
print()
# print(match.__repr__)
print(match.loser.wicketsLost, match.winner.wicketsLost)
print(match.winner.runs, match.winner)
print(match.loser.runs, match.loser)
# print(len(crickit.Teams.allteamobjects))
# print(simulatedMatch.matches[1].winner.runs)
# print(simulatedMatch.matches[2].winner.runs)
# print(simulatedMatch.matches[3].winner.runs)