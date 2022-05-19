def solution(s, n):
    answer=[]
    for i in s:
        if 65<=ord(i)<=90:
            if (ord(i)+n)%91 < 65:
                answer.append(chr(65+(ord(i)+n)%91))
            else:
                answer.append(chr(ord(i)+n%91))
        elif 97<=ord(i)<=122:
            if (ord(i)+n)%123 < 97:
                answer.append(chr(97+(ord(i)+n)%123))
            else:
                answer.append(chr(ord(i)+n%123))
        else:
            answer.append(i)
    return ''.join(answer)
