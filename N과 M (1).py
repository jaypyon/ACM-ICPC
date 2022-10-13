import sys
from itertools import permutations
input = sys.stdin.readline
N,M = map(int, input().split())
rst = list(permutations([i for i in range(1,N+1)],M))
for i in rst:
    print(" ".join(list([str(j) for j in list(i)])))
