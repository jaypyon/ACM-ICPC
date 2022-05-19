def solution(sizes):
    for size in sizes:
        if(size[0]<size[1]):
            size[0],size[1]=size[1],size[0]
    return max([i[0] for i in sizes])*max([i[1] for i in sizes])
