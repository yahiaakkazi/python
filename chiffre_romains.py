def romain_chiffre(n: int):
    assert 0<n<10
    L = ["I","II","III","IV","V","VI","VII","VIII","IX"]
    return L[n-1]

def romain_chiffre_generique(n: int, un: str, cinq: str, dix: str):
    assert 0<n<10
    L= [un,un+un,un+un+un,un+cinq,cinq,cinq+un,cinq+un+un,cinq+un+un+un,un+dix]
    return L[n-1]

def romain(n: int):
    asset 0<n<4000
    if 0<n<10:
        return romain_chiffre(n)
    else:
        i=0
        M=[0,0,0,0]
        print(M)
        while n>10:
            M[i]=n%10
            i=i+1
            n=n//10
        M[i]=n

        return M[-1]foisM+




