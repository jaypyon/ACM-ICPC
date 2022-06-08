import sys
from math import *
input = sys.stdin.readline
N = int(input())
liquid = list(map(int,input().split()))
liquid.sort()
pointer1, pointer2 = 0,N-1
min_val, min_pointers =2000000001,[-1,-1]
while(pointer1<pointer2 and pointer1<N and pointer2>0):
    comp_val = liquid[pointer1] + liquid[pointer2]
    if abs(comp_val)<=abs(min_val):
        min_val, min_pointers = comp_val,[str(liquid[pointer1]),str(liquid[pointer2])]
    
    if comp_val==0:
        break
    elif comp_val > 0:
        pointer2-=1
    else:
        pointer1+=1
    
print(" ".join(min_pointers))
