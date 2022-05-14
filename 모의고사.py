def solution(answers):
    answer=[]
    num1 = [1, 2, 3, 4, 5] #length:5 index:mod-5
    num2 = [2, 1, 2, 3, 2, 4, 2, 5] #length:8 index:mod-8
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #length:10 index:mod-10
    res = [[1,0],[2,0],[3,0]]
    for i,ans in enumerate(answers):
        if(ans == num1[i%5]):
            res[0][1]+=1
        if(ans == num2[i%8]):
            res[1][1]+=1
        if(ans == num3[i%10]):
            res[2][1]+=1
    res=sorted(res,key=lambda x:-x[1])
    max=res[0][1]
    for num in res:
        if(num[1]==max):
            answer.append(num[0])
    return sorted(answer)
