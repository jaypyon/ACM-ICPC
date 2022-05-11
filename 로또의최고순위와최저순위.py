def solution(lottos, win_nums):
    zero = 0
    win = 0
    for lotto in lottos:
        if lotto==0:
            zero+=1
        else:
            if lotto in win_nums:
                win+=1
    if(win==0 and zero ==6):
        return [1,6]
    elif(win==0 and zero == 0):
        return [6,6]
    else:
        return [7-win-zero, 7-win]
