import cv2
import mediapipe as mp
import math,numpy as np
import threading
import random
from probabilities import Model
model = Model()
previousMove = 0
moves = []
next_move = []
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
hands =  mp_hands.Hands()
count = 0
timer = 0
total = 0
s1 = ""
s2 = ""
def isScissors():
    point_4 = ()  # tip of thumb
    point_16 = ()  # tip of ring finger
    point_8 = () #tip of index fingerq
    point_12 = () #tip of middle finger
    (h, w, c) = image.shape
    for id, lm in enumerate(landMarks.landmark):
        if id == 4:
            point_4 = (int(lm.x * w), int(lm.y * h))
        if id == 16:
            point_16 = (int(lm.x * w), int(lm.y * h))
        if id == 8:
            point_8 = (int(lm.x * w), int(lm.y * h))
        if id == 12:
            point_12 = (int(lm.x * w), int(lm.y * h))
    # cv2.circle(image, point_4, 20, (0, 0, 233), -1)
    # cv2.circle(image, point_16, 20, (0, 0, 233), -1)
    # cv2.circle(image, point_12, 20, (0, 0, 233), -1)
    # cv2.circle(image, point_8,20, (0, 0, 233), -1)
    # print(math.dist(point_8,point_12),math.dist(point_4, point_16))
    return math.dist(point_4, point_16) <= 35 and math.dist(point_8,point_12)>=35 and math.dist(point_8,point_12)<=140
def change(predictedMove,actualMove):
    global previousMove
    # print("Actual Move-",actualMove)
    model.changeTrasitionMatrix(actualMove, predictedMove, previousMove)
    model.nextState()
    previousMove = actualMove

def predict():
    predictedMove = model.predict()
    # print("Predicted Move-", predictedMove)
    return predictedMove

def isPaper():
    point_5 = ()
    point_9 = ()
    point_13 = ()
    point_17 = ()
    point_16 = ()  # tip of ring finger
    point_8 = ()  # tip of index finger
    point_12 = ()  # tip of middle finger
    point_20 = () # tip of pinky finger
    (h, w, c) = image.shape
    for id, lm in enumerate(landMarks.landmark):
        if id == 5:
            point_5 = (int(lm.x * w), int(lm.y * h))
        if id == 9:
            point_9 = (int(lm.x * w), int(lm.y * h))
        if id == 13:
            point_13 = (int(lm.x * w), int(lm.y * h))
        if id == 17:
            point_17 = (int(lm.x * w), int(lm.y * h))
        if id == 16:
            point_16 = (int(lm.x * w), int(lm.y * h))
        if id == 8:
            point_8 = (int(lm.x * w), int(lm.y * h))
        if id == 12:
            point_12 = (int(lm.x * w), int(lm.y * h))
        if id == 20:
            point_20 = (int(lm.x * w), int(lm.y * h))
    # cv2.circle(image, point_16, 20, (0, 0, 233), -1)
    # cv2.circle(image, point_12, 20, (0, 0, 233), -1)
    # cv2.circle(image, point_8,20, (0, 0, 233), -1)
    # cv2.circle(image, point_20, 20, (0, 0, 233), -1)
    # print(math.dist(point_5,point_8),math.dist(point_9, point_12),math. dist(point_13,point_16),math.dist(point_17,point_20))
    return math.dist(point_5,point_8)>=140 and math.dist(point_5,point_8)<=210 and math.dist(point_9,point_12)>=160 and math.dist(point_9,point_12)<=231 and math.dist(point_13,point_16)>=150 and math.dist(point_13,point_16)<=215 and math.dist(point_17,point_20)>=95 and math.dist(point_17,point_20)<=180
    # return math.dist(point_4,point_8)>=180 and math.dist(point_4, point_12)>=230 and math.dist(point_4, point_12)<=350 and math.dist(point_4, point_16)>=250 and math.dist(point_4, point_16)<=370 and math.dist(point_4, point_20)>=260
def isRock():
        point_4 = ()  # tip of thumb
        point_16 = ()  # tip of ring finger
        point_8 = ()  # tip of index finger
        point_12 = ()  # tip of middle finger
        point_20 = ()  # tip of pinky finger
        (h, w, c) = image.shape
        for id, lm in enumerate(landMarks.landmark):
            if id == 4:
                point_4 = (int(lm.x * w), int(lm.y * h))
            if id == 16:
                point_16 = (int(lm.x * w), int(lm.y * h))
            if id == 8:
                point_8 = (int(lm.x * w), int(lm.y * h))
            if id == 12:
                point_12 = (int(lm.x * w), int(lm.y * h))
            if id == 20:
                point_20 = (int(lm.x * w), int(lm.y * h))
        # cv2.circle(image, point_4, 20, (0, 0, 233), -1)
        # cv2.circle(image, point_16, 20, (0, 0, 233), -1)
        # cv2.circle(image, point_12, 20, (0, 0, 233), -1)
        # cv2.circle(image, point_8, 20, (0, 0, 233), -1)
        # cv2.circle(image, point_20, 20, (0, 0, 233), -1)
        # print(math.dist(point_8, point_12), math.dist(point_12, point_16),
        #       math.dist(point_16, point_20))
        return math.dist(point_8, point_12) >= 20 and math.dist(point_8, point_12) <=40 and math.dist(point_12, point_16)>=20 and math.dist(point_12, point_16)<=40 and math.dist(point_16, point_20)>=20 and math.dist(point_16, point_20)<=40
previousMove = -1
predictedMove = -1
while cap.isOpened():
    success, image = cap.read()
    image.flags.writeable = False
    image = cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_RGB2BGR)
    results = hands.process(image)
    image.flags.writeable = True
    actualMove = -1
    if results.multi_hand_landmarks:
        for landMarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image,landMarks,mp_hands.HAND_CONNECTIONS)
            if (isScissors()):
                total += 1
                actualMove = 2
                print("Scissors")

            elif (isPaper()):
                actualMove = 1
                total += 1
                print("Paper")
            elif (isRock()):
                actualMove = 0
                total += 1
                print("Rock")
            else:actualMove = -1
            predictedMove = predict()
            # print(count, total, actualMove, predictedMove)
            change(predictedMove, actualMove)
            if predictedMove == actualMove:
                count += 1
    if predictedMove == 0: predictedMove = "Rock"
    if predictedMove == 1: predictedMove = "Paper"
    if predictedMove == 2: predictedMove = "Scissors"
    if actualMove == 0: actualMove = "Rock"
    if actualMove == 1: actualMove = "Paper"
    if actualMove == 2: actualMove = "Scissors"
    if actualMove !=-1:
        s1 = "Predicted:"+str(predictedMove)
        s2 = "Actual:"+str(actualMove)
    cv2.putText(image, s1, (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(image, s2, (10, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    if total>0:
        cv2.putText(image, "Accuracy:" + str(count / total), (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow("Rock Paper Scissors prediction",image)
    if cv2.waitKey(1) == ord('q'):
        break
print(count/total)