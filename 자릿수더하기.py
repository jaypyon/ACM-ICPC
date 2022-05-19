# Iterable Solution
def solution(n):
    answer=0
    count = 0
    while(10**count<=n):
        count+=1
    for i in range(count-1,-1,-1):
        digit = 1
        while(n-digit*(10**i)>=0):
            digit+=1
        answer += digit-1
        print(answer)
        n-=(digit-1)*(10**i)
    return answer

# Recursive Solution
def solution(n):
    if n<10:
        return n
    else:
        return n%10 + solution(n//10)
# Type Conversion Solution
def solution(n):
    return sum([int(i) for i in str(n)])
