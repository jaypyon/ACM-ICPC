def solution(n):
    criteria = 0
    answer = 0
    
    while(3**criteria<=n):
        criteria+=1
    tenary = [0 for _ in range(0,criteria)]
    for i in range(criteria-1,-1,-1):
        
        for j in range(0,2):
            if n-3**i >= 0:
                n-=3**i
                tenary[i]+=1
    for i,v in enumerate(tenary):
        answer+=v*3**(len(tenary)-1-i)

    return answer
