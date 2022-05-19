def solution(phone_number):
    return ''.join(['*' for _ in range(0,len(phone_number)-4)])+phone_number[len(phone_number)-4:len(phone_number)]
