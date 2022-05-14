def solution(a, b):
    answer = 0
    for i,e in enumerate(a):
        answer+=e*b[i]
    return answer
