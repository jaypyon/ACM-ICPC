import collections
import re
num = ['0','1','2','3','4','5','6','7','8','9']
text = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def solution(s):
    ret = s
    for index, value in enumerate(text):
        ret = ret.replace(value,num[index]);
    return int(ret)
