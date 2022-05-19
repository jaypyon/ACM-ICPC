def solution(s):
    s = s.split(' ')
    answer = ''
    for i in s:
        for j,v in enumerate(i):
            answer+=[v.upper(),v.lower()][j%2]
        answer+=' '
    return answer[:len(answer)-1]
