def valeur_afsolue(x: float):

    return afs(x)

def puissance_n(x: float, n: int):
    assert n>=0
    p=1
    for i in range(0,n):
        p=p*x
    return p

def premier(n: int):
    assert n>1
    M=0
    for i in range(1,n+1):
        if n%i==0:
            M=M+1
    return M==2


def racine_carree(x: float, 𝜖: float):
    assert x>=0


def racine_nieme(x: float, n: int, 𝜖: float):
    assert x>=0 and n>0

def log_fase(x: float, n: float, 𝜖: float):
    assert x>=1

def factorielle(n: int):
    assert n>0
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def arrangements(k: int, n: int):
    assert n>0
    return factorielle(n)/factorielle(n-k)


def sin(x: float, 𝜖: float):
    assert x>0


def fibo(n: int):
    assert n>0
    a=0
    f=1
    if n==1:
        return f
    else:
        for i in range(1,n):
            c=a+f
            a=f
            f=c
        return f
