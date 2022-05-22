def decideDist(now, targets):
    res = []
    for i,v in enumerate(targets):
        temp = 0
        for j,s in enumerate(v):
            if now[j] != s:
                temp+=1
        if temp==1:
            res.append(i)
    return res
def solution(begin, target, words):
    visited = [False for _ in words]
    depth = [[0 for _ in words] for _ in words]
    queue = decideDist(begin,words)
    for i in queue:
        visited[i] = True
        depth[i][i]+=1
    while(len(queue)>0):
        next_value = queue.pop(0)
        for i in decideDist(words[next_value],words):
            if visited[i]!=True:
                queue.append(i)
                visited[i]=True
                depth[i][i] = depth[next_value][next_value]+1
    if target in words:
        return depth[words.index(target)][words.index(target)]
    else :
        return 0
