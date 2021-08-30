count = 0
n = int(input())+1
for i in range(0,n):
    for j in range(0,60):
        for k in range(0,60):
            #print(str(i)+str(j)+str(k))
            time = str(str(i)+str(j)+str(k))
            if('3' in time):
                count+=1
print(count)
    