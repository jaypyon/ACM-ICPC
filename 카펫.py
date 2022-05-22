def solution(brown, yellow):
    for h in range(0,brown//2):
        for w in range(h,brown//2):
            if(h*w==brown+yellow and (h-2)*(w-2)==yellow):
                return sorted([h,w],key= lambda x:-x)
