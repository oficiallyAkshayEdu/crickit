# from PlayCricket import *
# import sys, os
#
# # Disable
# def blockPrint():
#     sys.stdout = open(os.devnull, 'w')
#
# # Restore
# def enablePrint():
#     sys.stdout = sys.__stdout__
#
# simulateCount = 1000
#
# class Simulator:
#     def __init__(self):
#         self.t1_wins = 0
#         self.t2_wins = 0
#         self.ties = 0
#
# if __name__ == "__main__":
#     blockPrint()
#     # simulate = Simulator()
#     for i in range(simulateCount):
#         playMatch(India, Pakistan)
#         if winner == India:
#             IndiaWinCount += 1
#         elif winner == Pakistan:
#             PakistanWinCount += 1
#         else:
#             tieCount = +1
#     print("\n")
#     enablePrint()
#     print("A total of {} matches were played".format(simulateCount))
#     print("India won {}% ({}) matches, Pakistan won {}% ({}) Matches. {}% ({}) Matches were tied".format(
#         (IndiaWinCount * 100) / simulateCount, IndiaWinCount, (PakistanWinCount * 100) / simulateCount, PakistanWinCount,
#         (tieCount * 100) / simulateCount, tieCount))
#
