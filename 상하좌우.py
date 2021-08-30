def isInSize(size, point):
    if(point[0]>0 and point[1]>0 and point[0]<=size and point[1]<=size):
        return True
    else: return False

direction = dict({
    "L":[0,-1],
    "R":[0,1],
    "U":[-1,0],
    "D":[1,0]
})
startpoint = [1,1];
inputSize = int(input())
inputString = input().split()

for dir in inputString:
    if(isInSize(inputSize,[startpoint[0]+direction[dir][0],startpoint[1]+direction[dir][1]])):
        startpoint[0]+=direction[dir][0]
        startpoint[1]+=direction[dir][1]

print(startpoint)