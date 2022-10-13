from collections import defaultdict
import re
answer = []
names = defaultdict()
actions = {
    'Enter':'님이 들어왔습니다.',
    'Leave':'님이 나갔습니다.'
}
def solution(record):
    for r in record:
        splitedRecord = list(map(str,r.split()))
        if splitedRecord[0] != 'Leave':
            names[splitedRecord[1]]=splitedRecord[2]
        if splitedRecord[0] == 'Leave' or splitedRecord[0] == 'Enter':
            answer.append("{0}{1}".format(splitedRecord[1],actions[splitedRecord[0]]))
    
    regex = r'^[a-zA-Z0-9]+'
    for i,a in enumerate(answer):
        userID=re.findall(regex,a)[0]
        answer[i] = a.replace(userID,names[userID])
    return answer

#Muzi가 나간후 다시 들어올 때, Prodo 라는 닉네임으로 들어올 경우 기존에 채팅방에 남아있던 Muzi도 Prodo로 다음과 같이 변경된다. 무지를 트래킹해야함.
