# 처음 풀이
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

# 재귀구조를 이용한 풀이
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 
print("결과 : {}".format(sum_digit(123)));
