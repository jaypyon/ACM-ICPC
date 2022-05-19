import re
def solution(s):
    if re.match(r'^(?=[0-9]*$)(?:.{4}|.{6})$',s):
        return True
    else: return False
