def racines_2nd_degre(a: float, b: float, c: float):
"""
:entrée a: float
:entrée b: float
:entrée c: float
:pré-cond: a ̸= 0
:sortie r1: float ou None
:sortie r2: float ou None
:post-cond: si l'équation ax2+bx + c n'a pas de racine réelle,
r1 = r2 = None,
sinon, si elle a exactement une racine réelle,
r1 a pour valeur cette racine et r2 = None,
sinon (l'équation a deux racine réelles),
r1 et r2 ont pour valeur ces deux racines,
avec r1 > r2
"""
    assert a!=0
    delta=b**2-4*a*c
    if delta<0:
        return (None,None)
    elif delta==0:
        return (-b/2*a, None)
    else:
        return ((-b-np.sqrt(delta))/(2*a),(-b+np.sqrt(delta))/(2*a))
