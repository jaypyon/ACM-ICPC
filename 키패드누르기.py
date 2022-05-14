import collections
from math import * 
keypads=[1,2,3,4,5,6,7,8,9,0]
keypositions=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,1]]
keyposition=dict(zip(keypads,keypositions))
print(keyposition)
right = [3,2]
left =[3,0]
mainHand = 'R'
def theDistanceFromHands(targetNumber):
    global keypads
    global keyposition
    global right
    global left
    retValue = ''
    if(targetNumber in [1,4,7]):
        retValue = 'L'
    elif(targetNumber in [3,6,9]):
        retValue = 'R'
    elif(targetNumber in [2,5,8,0]):
        distSquareFromLeft = sqrt((keyposition[targetNumber][0]-left[0])**2) + sqrt((keyposition[targetNumber][1]-left[1])**2)
        distSquareFromRight = sqrt((keyposition[targetNumber][0]-right[0])**2) + sqrt((keyposition[targetNumber][1]-right[1])**2)
        if(distSquareFromLeft == distSquareFromRight):
            retValue = mainHand
        elif(distSquareFromLeft < distSquareFromRight):
            retValue = 'L'
        elif(distSquareFromLeft > distSquareFromRight):
            retValue = 'R'
    if(retValue == 'R'):
        right = keyposition[targetNumber]
    elif(retValue == 'L'):
        left = keyposition[targetNumber]
    
    return retValue
def solution(numbers, hand):
    global mainHand
    answer = ''
    if(hand=='right'):
        mainHand = 'R'
    if(hand=='left'):
        mainHand = 'L'
    for i in numbers:
        answer+=theDistanceFromHands(i)
    return answer
