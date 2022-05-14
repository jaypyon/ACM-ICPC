def solution(d, budget):
    answer = 0
    d = sorted(d)
    crit = 0
    for i in d:
        crit+=i
        if crit > budget:
            break;
        answer+=1
    return answer
