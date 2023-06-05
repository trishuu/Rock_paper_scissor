"""
ANOLOGIES THAT HAS BEEN USED
0 - Rock
1 - Paper
2 - Scissors
"""
class Model:
    def __init__(self,baisFactor = 0.1):
        self.P = [[1/3,1/3,1/3] for i in range(3)]
        self.S = [[1,0,0]]
        self.predictedMove = 0
        self.previousMove = 0
        self.biasFactor = baisFactor

    def changeTrasitionMatrix(self, actualMove,predictedMove,previousMove):
        if actualMove == predictedMove:
            print("Correctly Predicted")
            for currentPossibility in range(3):
                if currentPossibility == predictedMove:
                    self.P[previousMove][predictedMove] += self.biasFactor
                    if self.P[previousMove][predictedMove] < 0:
                        self.P[previousMove][predictedMove] = 0
                    if self.P[previousMove][predictedMove] >= 1:
                        self.P[previousMove][predictedMove] = 1
                else:
                    self.P[previousMove][currentPossibility] -= self.biasFactor / 2
                    if self.P[previousMove][currentPossibility] < 0:
                        self.P[previousMove][currentPossibility] = 0
                    if self.P[previousMove][currentPossibility] >= 1:
                        self.P[previousMove][currentPossibility] = 1
        else:
            for currentPossibility in range(3):
                if currentPossibility == predictedMove:
                    self.P[previousMove][predictedMove] -= self.biasFactor
                    if self.P[previousMove][predictedMove] < 0:
                        self.P[previousMove][predictedMove] = 0
                    if self.P[previousMove][predictedMove] >= 1:
                        self.P[previousMove][predictedMove] = 1
                else:
                    self.P[previousMove][currentPossibility] += self.biasFactor / 2
                    if self.P[previousMove][currentPossibility] < 0:
                        self.P[previousMove][currentPossibility] = 0
                    if self.P[previousMove][currentPossibility] >= 1:
                        self.P[previousMove][currentPossibility] = 1

    def nextState(self):
        result = [[0, 0, 0]]
        for i in range(len(self.S)):
            for j in range(len(self.P)):
                for k in range(len(self.P)):
                    result[i][j] += self.S[i][k] * self.P[k][j]

        self.S = result
    def predict(self):
        return self.S[0].index(max(self.S[0]))


Trisha = Model()
# previousMove = 0
# while True:
#     print("Transition Matrix ",Trisha.P)
#     print("State Matrix ",Trisha.S)
#     predictedMove = Trisha.predict()
#     print("Predicted Move-",predictedMove)
#     actualMove = int(input("Acutual Move-"))
#     Trisha.changeTrasitionMatrix(actualMove,predictedMove,previousMove)
#     Trisha.nextState()
#     previousMove = actualMove