from collections import deque
dir=[[0,-1],[0,1],[-1,0],[1,0]]#상 하 좌 우
def isAllVisited(graph):
    for i in graph:
        for j in i:
            if j==0:
                return False
    return True
def isInSize(x,y,graph):
    horMost = len(graph[0])
    verMost = len(graph)
    if -1<y<horMost and -1<x<verMost:
        return True
    return False
def bfs(x,y,visited):
    queue=deque()
    level=0
    for i,y in enumerate(visited):
        for j,x in enumerate(y):
            if(x == 1):
                visited[i][j] = 1
                queue.append([i,j])
    while queue:
        sz = len(queue)
        for _ in range(sz):
            now = queue.popleft()
            for d in dir:
                if isInSize(now[0]+d[0],now[1]+d[1],graph) and visited[now[0]+d[0]][now[1]+d[1]]==0 and visited[now[0]+d[0]][now[1]+d[1]]!=-1:
                    visited[now[0]+d[0]][now[1]+d[1]] = 1
                    queue.append([now[0]+d[0],now[1]+d[1]])
        level+=1
    if isAllVisited(visited): return level-1
    else: return -1
    
def solution(graph):
    print(bfs(0,0,graph))

a,b = map(int,input().split())
graph = [list(map(int,input().split())) for j in range(b)]
solution(graph)
