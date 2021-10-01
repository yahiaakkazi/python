def compte_chiffres(n: int):
    assert n>=10
    c=1
    while n>=10:
        c=c+1
        n=n//10
    return c

def somme_chiffres(n: int):
    assert n>0
    c=0
    for i in range(0,len(str(n))):
        c=c+int(str(n)[i])
    return c

def compte_chiffre(n: int, c: int):
    assert n>0 and 0<=c<=9
    nc=0
    for i in range(0,len(str(n))):
        if str(n)[i]==str(c):
            nc=nc+1
    return nc

def compte_chiffres_pairs(n: int):
    assert n>=0
    c=0
    for i in range(0,len(str(n))):
        if int(str(n)[i])%2==0:
            c=c+1
    return c

def chiffre_au_rang(n: int, i: int):
    assert n>10**i
    return int(str(n)[i])

def rang_max(n: int, c: int):
    assert n>0 and 0<=c<=9
    r=-1
    for i in range(0,len(str(n))):
        if str(n)[i]==str(c):
            r=i
    return r

def rang_min(n: int, c: int):
    assert n>0 and 0<=c<=9
    r=-1
    R=[]
    for i in range(0,len(str(n))):
        if str(n)[i]==str(c):
            R=R+[i]
    if R==[]:
        return r
    else:
        return R[0]
