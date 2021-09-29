def factorielle(x:int) -> int:
    if x==0:
        return 1
    else:
        return x*factorielle(x-1)