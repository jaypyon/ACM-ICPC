import sys
input = sys.stdin.readline
N,S = map(int,input().split())
total_list = list(map(int,input().split()))
pointer1,pointer2 = -1,0
local_sum=total_list[pointer2]
min_len = 2147483647
cache1, cache2 = 0,0
while(pointer2<N):
    if local_sum >= S:
        sub_len = pointer2 - pointer1
        if min_len > sub_len:
            min_len = sub_len
        
        if pointer1<pointer2:
            pointer1+=1
            local_sum-=total_list[pointer1]
        else:
            if pointer2<N-1:
                pointer2+=1
                local_sum+=total_list[pointer2]
            else:
                pointer2+=1
    else:
        if pointer2<N-1:
            pointer2+=1
            local_sum+=total_list[pointer2]
        else:
            pointer2+=1

if min_len ==0:
    min_len = 1
if min_len ==2147483647:
    min_len = 0
print(min_len)
