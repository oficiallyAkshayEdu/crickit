import crickit

match = crickit.playMatch("India","Pakistan")
simulatedMatch = crickit.simulateMatches("India","Pakistan", 100)

print('\n')
# print(match.matchSummary())
print(match)
# print(simulatedMatch)