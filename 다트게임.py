import re
def solution(dartResult):
    darts = re.findall(r'[0-9]+[SDT][*#]?',dartResult)
    results =[0 for _ in darts]
    for index,dart in enumerate(darts):
        local =int(re.sub(r'[SDT*#]','',dart))
        for factor in dart:
            if  factor.isalpha():
                if factor=='D':
                    local= local**2
                elif factor=='T':
                    local= local**3
            else:  
                if factor=='*':
                    if(index>0):
                        results[index-1]*=2
                    local*=2
                elif factor=='#':
                    local*=-1
        results[index]=local;
    return sum(results)
