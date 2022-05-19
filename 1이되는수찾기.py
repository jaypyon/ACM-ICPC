def solution(n):
    answer = 1
    remainder = 0
    while(remainder!=1):
        answer+=1
        remainder = n%answer
    return answer
