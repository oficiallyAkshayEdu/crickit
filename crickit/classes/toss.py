class Toss():
    def __init__(self):
        self.calledFace = ""
        self.winner = []
        self.calledBy = []
        self.loser = []  # TODO store who loses the toss
        self.faceUp = []
        self.coinFaces = ["Heads", "Tails"]