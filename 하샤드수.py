def solution(x):
    answer = x%sum([int(i) for i in str(x)])
    if(answer ==0 ):
        return True
    else: return False
