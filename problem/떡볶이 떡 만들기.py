M, N = map(int,input().split())
print(M,N)

ricecake = list(map(int,input().split()))
max = max(ricecake)

start=0
end = max
result =0
while start<=end:
    height = (start+end)//2
    localRes=0
    for i in ricecake:
        if(i-height>0):
            localRes+=(i-height)
            #print(localRes)
    print(localRes)    
    if (localRes-N)<0:
        print(localRes, start, end)
        end = height-1
    else:
        print(localRes, start, end)
        result = height
        start = height+1 

print(result)
