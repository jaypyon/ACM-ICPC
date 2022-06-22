from collections import defaultdict
DP = defaultdict(set)
def solution(N, number):
    for i in range(1,10):
        DP[i].add(int(str(N)*i))
    for i in range(2,9):
        for j in range(1,i):
            for k in range(1,i):
                if j+k == i:
                    for f in list(DP[j]):
                        for s in list(DP[k]):
                            DP[i].add(f*s)
                            if f/s > 0:
                                DP[i].add(f/s)
                            DP[i].add(f+s)
                            if f-s > 0:
                                DP[i].add(f-s)
    
    for i in range(1,9):
        for j in DP[i]:
            if j == number:
                return i
    return -1
