N=int(input())
M=int(input())
frame = [[] for _ in range(0,N)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def checkRoutine(i,j):
    for k in range(0,4):
        if(i+dx[k]<0 or i+dx[k]>=N or j+dy[k]<0 or j+dy[k]>=M):continue
        if frame[i+dx[k]][j+dy[k]] == 0:
            frame[i+dx[k]][j+dy[k]]=1
            checkRoutine(i+dx[k],j+dy[k])
def DFS():
    count = 0
    for i in range(0,N):
        for j in range(0,M):
            if frame[i][j] == 0:
                count+=1
                checkRoutine(i,j)

    return count
                

if __name__=="__main__":
    for i in range(0,N):
        tempString = input()
        for j in tempString:
            frame[i].append(int(j))
    print(frame)  
    print(DFS())
    
