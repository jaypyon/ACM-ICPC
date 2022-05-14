import collections
import re
num = ['0','1','2','3','4','5','6','7','8','9']
text = ["zero","one","two","three","four","five","six","seven","eight","nine"]
ntotMap = dict(zip(text,num))

def solution(s):
    answer = s
    s = re.findall(r'[^0-9]+',s)
    print(s)
    if(len(s)>0):
        for i in s:
            if(len(i)<=5):
                answer = answer.replace(i,ntotMap[i])
            else:
                while(len(i)>0):
                    #3
                    if(i[0:3] in text):
                        answer = answer.replace(i[0:3],ntotMap[i[0:3]],1)
                        i=i[3:]
                    #4
                    elif(i[0:4] in text):
                        answer = answer.replace(i[0:4],ntotMap[i[0:4]],1)
                        i=i[4:]
                    #5
                    elif(i[0:5] in text):
                        answer = answer.replace(i[0:5],ntotMap[i[0:5]],1)
                        i=i[5:]

    return int(answer)
