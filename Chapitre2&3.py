def compte_car(s: str, c: str) -> int:
    assert len(c)==1
    n=0
    for i in s:
        if i==c:
            n=n+1
    return n

def compte_minuscules(s: str) -> int:
    n=0
    for i in s:
        if str.islower(i):
            n=n+1
    return n


def indice_min_car(s: str, c: str) -> int:
    assert len(c)==1
    imin=[]
    for i in range(0,len(s)):
        if s[i]==c:
            imin=imin+[i]
    return imin[0]


def indice_max_car(s: str, c: str) -> int:
    assert len(c)==1
    imax=[]
    for i in range(0,len(s)):
        if s[i]==c:
            imax=imax+[i]
    return imax[-1]

def indice_suivant_car(s: str, c: str, ig: int) -> int:
    assert len(c)==1
    x=[]
    for i in range(ig+1,len(s)):
        if s[i]==c:
            x=x+[i]
    return x[0]

def indice_prec_car(s: str, c: str, id: int) -> int:
    assert len(c)==1



def commence_par(s: str, t: str) -> bool:
    for i in range(0,len(s)):
        assert s[i]==t[i]
    return True

def indice_min(s: str, t: str) -> int:
    imin=0
    assert True


def indice_max(s: str, t: str) -> int:
    assert True

def indice_suivant(s: str, t: str, ig: int) -> int:
    assert len(c)==1

def indice_prec(s: str, t: str, id: int) -> int:
    assert len(c)==1

def inverse(s: str) -> str:
    n=""
    for i in range(1,len(s)+1):
        n=n+s[-1*i]

    return n

def palindrome(s: str) -> bool:
    n=True
    for i in range(0,len(s)):
        if s[i]!=s[-i-1]:
            n=False
    return n


def compte_mots(s: str) -> int:
    return len(str.split(s))


def bien_parenthesee(txt: str) -> bool:
    s=0
    for i in txt:
        if i=="(":
            s=s+1
    for i in txt:
        if i==")":
            s=s-1
    return s==0


def eval_binaire(txt: str) -> int:
    int=0
    s=0
    for i in txt:
        assert i in ["0","1"]
    for i in inverse(txt):
        if i=="0":
            s=s+1
        else:
            int=int+2**s
            s=s+1
    return int


def eval_decimal(txt):
    for i in txt:
        assert i in ["0","1"]

def repr_binaire(val: int) -> str:
    assert val>=0


def repr_decimal(val: int) -> str:
    assert val>=0

def repr_hexadecimal(val: int) -> str:
    assert val>=0

def decompresse(comp: str) -> str:
    decomp=""
    #s=0
    assert len(comp)%2==0
    for i in range(0,len(comp)):
        if i%2==0:
            assert comp[i] in ["0","1","2","3","4","5","6","7","8","9"]
            #s=i
            decomp=decomp+int(comp[i])*comp[i+1]
    return decomp

def compresse(txt: str) -> str:
    assert len(txt)%2==0



def indice_prec_car(s: str, c: str, id: int) -> int:
    assert a>=0 and b>=0 and c>=0
    return min(a,b,c)**max(a,b,c)