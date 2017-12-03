import crickit

match = crickit.playMatch("India","Pakistan")
print(match.winner.runScore)

simulatedMatch = crickit.simulateMatches("India","Pakistan", 100)
print('\n')
print(simulatedMatch.t1_wins)
print(match.toss)

