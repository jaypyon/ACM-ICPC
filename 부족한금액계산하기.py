def solution(price, money, count):
    print([sum([i for i in range(1,2502)][:j]) for j in range(1,2502)])
    table=price*[sum([i for i in range(1,2502)][:j]) for j in range(1,2502)][count-1]-money
    if table<0:
        table=0
    return table
