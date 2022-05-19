def solution(num):
    count = 0
    while(count<500 and num!=1):
        num=[num/2,3*num+1][int(num)&1]
        count+=1
    if(count>=500): 
        return -1
    else:
        return count
