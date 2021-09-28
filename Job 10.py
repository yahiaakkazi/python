def arrondies(x:int) -> int:
    if abs(x%5-5)<3:
        return x-x%5+5
    else:
        return x

def notes(L:list) -> list:
    M=[]
    for i in L:
        M=M+[arrondies(i)]
    return M

