#Tournament

elit8 = ['URG', 'FRA', 'BRA', 'BEA', 'SWE', 'ENG', 'RUS', 'CRO']

def Champion(s, e):

    if (s == e):
        return s

    m = (s+e)//2

    Lwinner = Champion(s,m)
    Rwinner = Champion(m+1,e)

    return Lwinner,Rwinner
print(Champion(0,7))
