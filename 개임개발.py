direction = dict({
    0:[-1,0],#북
    1:[0,1], #동
    2:[1,0], #남
    3:[0,-1] #서
})
sizeY,sizeX = map(int,input().split())
startPoint = [0,0]
startPoint[0],startPoint[1],newDir = map(int,input().split())

world = list()
for y in range(0,sizeY):
    tempList = input().split()
    world.append(tempList)
sum = 1
count = 0

print(world)
def turnLeft(now):
    return (now+3)%4
def isInSize(position):
    if position[0]<sizeY and position[1]<sizeX and position[0]>=0 and position[1]>=0:
        if(world[position[0]][position[1]] == '0'):
            world[position[0]][position[1]]='1'
            return True
    return False


while True:
    
    newDir = turnLeft(newDir)
    count +=1
    if(isInSize([startPoint[0] + direction[newDir][0],startPoint[1]+ direction[newDir][1]])):
        startPoint[0] += direction[newDir][0]
        startPoint[1] += direction[newDir][1]
        count = 0
        sum+=1
        continue
    if (count == 4):
        if world[startPoint[0] - direction[newDir][0]][startPoint[1]- direction[newDir][1]]=="1": break
        else :
            startPoint[0] -= direction[newDir][0]
            startPoint[1] -= direction[newDir][1]
            count = 0;

print(sum)