import re
def solution(s):
    if len(re.findall(r'[p]', s.casefold()))==len(re.findall(r'[y]', s.casefold())):
           return True
    else:
           return False
