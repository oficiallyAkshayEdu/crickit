import crickit

match = crickit.playMatch("India","Pakistan")
simulatedMatch = crickit.simulateMatches("India","Pakistan", 10)

# print(match.loser.runScore, match.loser)
# print(match.winner.runScore, match.winner)
print()
# print(len(crickit.Teams.allteamobjects))
print(simulatedMatch.matches[1].winner.runScore)
print(simulatedMatch.matches[2].winner.runScore)
print(simulatedMatch.matches[3].winner.runScore)