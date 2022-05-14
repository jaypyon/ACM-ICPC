from itertools import * 
prime = [True for _ in range(0,3001)]
def eratos():
    global prime
    first = 2
    while(first<1501):
        second = 2
        criteria = first*second
        while(criteria<3001):
            prime[criteria]=False
            second+=1
            criteria = first*second
        first+=1
def solution(nums):
    global prime
    answer = 0
    eratos()
    for combination in list(combinations(nums,3)):
        if(prime[sum(combination)]):
            answer+=1
    return answer
