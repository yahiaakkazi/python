def tableaux_egaux(a: [int], b: [int]) -> bool:
    assert len(a)==len(b)
    a=True
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            b=False
    return a

def tableau_prefixe(a: [int], b: [int]) -> bool:
    assert len(a)>=len(b)
    a=True
    for i in range(0,len(b)):
        if a[i]!=b[i]:
            b=False
    return a

def tableau_palindrome(a: [int]) -> bool:
    b=True
    for i in range(0,len(a)):
        if a[i]!=a[len(a)-1-i]:
            b=False
    return b

def indice_min(a: [float]) -> int:
    assert len(a) > 0
    b=a[0]
    L=0
    for i in range(0,len(a)):
        if a[i]<=b:
            L=i
            b=a[i]
    return L


def indice_min_gauche(a: [float]) -> int:
    assert len(a) > 0
    b=a[0]
    L=0
    for i in range(0,len(a)):
        if a[i]<b:
            L=i
            b=a[i]
    return L

def indice_min_droite(a: [float]) -> int:
    assert len(a) > 0
    b=a[0]
    L=0
    for i in range(0,len(a)):
        if a[i]<=b:
            L=i
            b=a[i]
    return L


def indice_max(a: [float]) -> int:
    assert len(a) > 0
    b=a[0]
    L=0
    for i in range(0,len(a)):
        if a[i]>=b:
            L=i
            b=a[i]
    return L

def indice_gauche(a: [float], v: float) -> int:
    ival=-1
    for i in range(0,len(a)):
        if a[i]==v:
            ival=i
    return i

def indice_droite(a: [float], v: float) -> int:
    ival=[-1]
    for i in range(0,len(a)):
        if a[i]==v:
            ival=ival+[i]
    return ival[-1]

def indice_n(a: [float], v: float, n: int) -> int:
    assert n>0
    ival=[-1]
    for i in range(0,len(a)):
        if a[i]==v:
            ival=ival+[i]
    return ival[n]


def nb_occurences(a: [float], v: float) -> int:
    assert n>0
    ival=[]
    for i in range(0,len(a)):
        if a[i]==v:
            ival=ival+[i]
    return len(ival)

def somme(a: [float]) -> float:
    assert len(a)>0
    s=0
    for i in a:
        s=s+i
    return s

def moyenne(a: [float]) -> float:
    import statistics
    assert len(a)
    return statistics.mean(a)


def moyenne_ponderee(a: [float], poids: [float]) -> float:
    assert somme(poids)!=0 and len(poids)==len(a)
    s=0
    for i in range(0,len(a)):
        s=s+a[i]*poids[i]
    return s/somme(poids)


def premiers(n: int) -> [int]:
    assert n>0




