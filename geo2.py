def coerf_droite(x1:float, y1:float, x2: float, y2:float):

    assert x1!=x2
    a=(y2-y1)/(x2-x1)
    b=x2-a*x1
    return (a,b)