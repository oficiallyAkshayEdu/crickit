import crickit

match = crickit.playMatch("India","Pakistan")
# print(match.winner.runScore)

simulatedMatch = crickit.playMatch("India","Pakistan")
print('\n')
print(match)
print(simulatedMatch.winner)