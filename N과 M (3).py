import sys
input = sys.stdin.readline
N,M = map(int,input().split())
base = [1 for _ in range(M)]
def isBaseEnd(base,lim):
    for b in base:
        if b != lim:
            return False
    return True
def plusOne(base,N):
    base[-1]+=1
    count = 0
    for i in range(len(base)-1,-1,-1):
        if base[i] == N:
            base[i] = 1
            base[i-1]+=1
while not isBaseEnd(base,N):
    print(" ".join([str(i) for i in base]))
    plusOne(base,N+1)
print(" ".join([str(i) for i in base]))
