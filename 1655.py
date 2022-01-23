import sys
import heapq
input = sys.stdin.readline

leftheap,rightheap = [],[]
n = int(input())
for i in range(0,n):
    user = int(input())
    if(len(leftheap)==len(rightheap)):
        heapq.heappush(leftheap,-user)
    else:
        heapq.heappush(rightheap,user)

    if(len(leftheap)>0 and len(rightheap)>0 and -leftheap[0]>rightheap[0]):
        temp_left = -heapq.heappop(leftheap)
        temp_right = heapq.heappop(rightheap)
        heapq.heappush(leftheap,-temp_right)
        heapq.heappush(rightheap,temp_left)
    print(-leftheap[0])
