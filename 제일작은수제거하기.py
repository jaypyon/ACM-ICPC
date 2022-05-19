def solution(arr):
    answer = arr[:arr.index(min(arr))]+arr[1+arr.index(min(arr)):]
    if(len(answer)==0):
        answer.append(-1)
    return answer
