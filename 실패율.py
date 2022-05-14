def solution(N, stages):
    statistic = [[index+1,0,len(stages)] for index in range(0,N)]
    for stage in stages:
        if stage>N:
            continue    
        for j in range(stage,N):
            statistic[j][2]-=1
        statistic[stage-1][1]+=1
    def decision(x):
        if(x[2]==0):
            x[2]=1
            x[1]=0
        return -(x[1]/x[2])
    statistic = sorted(statistic,key=lambda x:decision(x))
    print(statistic)
    return [i[0] for i in statistic]
        
