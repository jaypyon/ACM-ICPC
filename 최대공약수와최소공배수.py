# 처음 풀이
def gcd(n,m):
    if(n>m):
        n,m=m,n
    if(n==0):
        return m
    else:
        return gcd(n,m%n)
def lcm(n,m):
    if(n>m):
        n,m=m,n
    count = 1
    while(n*count%m !=0):
        count+=1
    return n*count
def solution(n, m):
    answer = [gcd(n,m),lcm(n,m)]
    return answer
    
# 최소공배수 보완 풀이
def gcd(n,m):
    if(n>m):
        n,m=m,n
    if(n==0):
        return m
    else:
        return gcd(n,m%n)
def lcm(n,m,gcd):
    return n*m/gcd
def solution(n, m):
    gcd_euclidean = gcd(n,m)
    answer = [gcd(n,m),lcm(n,m,gcd_euclidean)]
    return answer
