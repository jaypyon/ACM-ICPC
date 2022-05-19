def solution(arr1, arr2):
    return [[v+arr2[i1][j] for j,v in enumerate(vi1)] for i1,vi1 in enumerate(arr1)]
