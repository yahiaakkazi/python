def duree_en_secondes(j: int, h: int, m: int, s: int):
    assert j>0 and h<24 and h>=0 and m>=0 and m<60 and s>=0 and s<60
    return s+m*60+h*60*60+j*60*60*24


#def secondes_en_duree(sec: int):

    #assert sec>=0


def ordre_heures(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int):

    assert 0<=h1<24 and 0<=m1<60 and 0<=s1<60 and 0<=h2<24 and 0<=m2<60 and 0<=s2<60
    return duree_en_secondes(0,h1,m1,s1)-duree_en_secondes(0,h2,m2,s2)

def difference_heures(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int):
    assert 0<=h1<24 and 0<=m1<60 and 0<=s1<60 and 0<=h2<24 and 0<=m2<60 and 0<=s2<60
    assert ordre_heures(h1, m1, s1, h2, m2, s2) >= 0
    return duree_en_secondes(0,h1,m1,s1)-duree_en_secondes(0,h2,m2,s2)


def decale_heure(h: int, m: int, s: int, d: int):
    assert 0<=h<24 and 0<=m<60 and 0<=s<60 and 0<=d<24*3600
    return secondes_en_duree(duree_en_secondes(0,h,m,s)+d)

def annee_bissextile(a: int):
    assert a>0
    return (a%4==0 and a%100!=0) or a%400==0

def jours_par_annee(a: int):
    assert a>0
    if annee_bissextile(a):
        return 366
    else:
        return 365

def jours_par_mois(m: int):
    assert 1<=m<=12
    #l'année donnée est non bissextile


def jours_par_annee_mois(a: int, m: int):
    assert a>0 and 1<=m<=12
    if annee_bissextile(a):
        if m==2:
            return 29
        else:
            return jours_par_mois(m)
    else:
        return jours_par_mois(m)

def ordre_dates(a1: int, m1: int, j1: int, a2: int, m2: int, j2: int):
    assert a1>0 and 1<=m1<=12 and a2>0 and 1<=m2<=12 and 1<=j1<jours_par_annee_mois(a1,m1) and 1<=j2<jours_par_annee_mois(a2,m2)
    if a1==a2:
        if m1==m2:
            return j1-j2
        elif m1>m2:
            return 1
        else:
            return -1
    elif a1>a2:
        return 1
    else:
        return -1

def decale_date (a: int, m: int, j: int, d: int):
    assert a>0 and 1<=m<=12 and 1<=j<jours_par_annee_mois(a,m) and d>=0


def difference_dates(a1: int, m1: int, j1: int, a2: int, m2: int, j2: int):
    assert a1>0 and 1<=m1<=12 and a2>0 and 1<=m2<=12 and 1<=j1<jours_par_annee_mois(a1,m1) and 1<=j2<jours_par_annee_mois(a2,m2) and ordre_dates(a1,m1,j1,a2,m2,j2)>=0

def jour_de_la_semaine(a: int, m: int, j: int):
    assert a>=1900 and 1<=m<=12 and 1<=j<jours_par_annee_mois(a,m)


