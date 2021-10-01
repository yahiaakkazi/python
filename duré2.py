def secondes_en_duree(sec: int):
"""
:entrée sec: int
:pré-cond: sec ≥ 0
:sortie j: int
:sortie h: int
:sortie m: int
:sortie s: int
:post-cond: sec est le nombre de secondes correspond à
une durée de j jours, h heures, m minutes et s secondes
avec j > 0 , 0 ≤ h < 24 , 0 ≤ m < 60, 0 ≤ s < 60 .
"""
    assert sec>=0
