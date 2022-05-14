from itertools import *
def solution(numbers):
    return sorted(set([sum(i) for i in combinations(numbers,2)]))
