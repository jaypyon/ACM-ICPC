import sys 
input = sys.stdin.readline
N,M = map(int, input().split())
totalList = list(map(int,input().split()))
dp = [i for i in totalList]
for i in range(1,len(dp)):
    dp[i] = dp[i-1]+dp[i]
for _ in range(M):
    start,end = map(int,input().split())
    start-=2
    end-=1
    if start<0:
        print(dp[end])
    else:
        print(dp[end]-dp[start])
