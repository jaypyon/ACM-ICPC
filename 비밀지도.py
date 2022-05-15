def solution(n, arr1, arr2):
    answer = []
    for index, a1 in enumerate(arr1):
        answer.append(a1|arr2[index])
    criteria=2
    count=0
    max_crit = max(answer)
    while(criteria**count<=max_crit):
        count+=1
    binary = [[' ' for _ in range(0,count)] for _ in range(0,len(answer)) ]
    
    for i,b in enumerate(answer):
        loc_count = count-1
        while(b>0):
            if(2**loc_count<=b):
                b-=2**loc_count
                binary[i][count-loc_count-1]='#'
            else:
                binary[i][count-loc_count-1]=' '
            loc_count-=1
        binary[i] = ''.join(binary[i])
    return binary
