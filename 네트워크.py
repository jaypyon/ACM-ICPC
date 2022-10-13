visited = []
computerNodes = []
def visiting(index):
    global visited
    global computerNodes
    for i,v in enumerate(computerNodes[index]):
        if v == 1 and visited[i] == 0 and index!=i:
            visited[i]=1
            visiting(i)
def solution(n, computers):
    global visited
    global computerNodes
    visited = [0 for i in range(0,n)]
    computerNodes = computers
    answer = 0
    for i in range(0,n):
        if(visited[i]==0):
            answer +=1
            visiting(i)
    return answer
