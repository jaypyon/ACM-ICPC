def myRoutine(n,k):
    count = 0
    temp = n
    while temp>1:
        if(temp%k == 0):
            count+=1
            temp=int(temp/k)
        elif(temp%k != 0):
            count+=1
            temp-=1
    return count

    
n,k = map(int, input().split())
print(myRoutine(n,k))