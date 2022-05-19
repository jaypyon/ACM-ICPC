def solution(s):
    divisor = [0 for _ in range(0,3001)]
    for i in range(1,3001):
        count = 1
        while(i*count<=3000):
            divisor[i*count]+=i
            count+=1
    return int(divisor[s])
