def solution(n):
    answer = [1 for i in range(0,n+1)]
    for i in range(2,int(n**0.5)+1):
        count=2
        while(i*count<=n):
            answer[i*count]=0
            count+=1
    return sum(answer[2:])
