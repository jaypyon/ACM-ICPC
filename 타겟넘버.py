def counting(depth,target,now,numbers):
    if(depth == len(numbers)):
        if(now == target):
            return 1
        else: return 0
    else:
        return counting(depth+1, target, now-numbers[depth],numbers)+counting(depth+1, target, now+numbers[depth],numbers)
    
def solution(numbers, target):
    answer = counting(0,target,0,numbers)     
    return answer
