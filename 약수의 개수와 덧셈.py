def solution(left, right):
    measure = [1 for _ in range(0,1001)]
    answer=0
    for i in range(2,1001):
        end = i
        count = 1
        while(end*count<1001):
            measure[end*count]+=1
            count+=1
    for i in range(left,right+1):
        if(measure[i]%2 == 0):
            answer+=i
        else:
            answer-=i
    return answer
