def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reportStat = [[0 for _ in range(len(id_list))] for _ in range(len(id_list))]
    for index,value in enumerate(report):
        [user,reporter] = value.split(' ')
        r_from = id_list.index(user)
        r_to = id_list.index(reporter)
        reportStat[r_to][r_from]=1
    for stat in reportStat:
        sum =0
        local_sender=[]
        for index,value in enumerate(stat):
            if value==1:
                local_sender.append(index)
                sum+=value
        if sum>=k:
            for sender in local_sender:
                answer[sender]+=1
    return answer
