from lf import lf
from fuz import fUz
from num import num

class Nstr:
    def __init__(self, arg, moo):
        self.x = arg
        self.y = moo
    def __sub__(self,other):
        c=self.x.replace(other.x,self.y)
        return c

def returh(a):
    pass

cses = {}
def priht(a):
    if a[0:6] == 'print:':
        if 'par' in a and ':;' in a:
            b = a.find('par')
            c = a.find(':;')
            d = Nstr(a,cses[a[b+4:c-1]])-Nstr(a[b:c+1],cses[a[b+4:c-1]])
            print(d[6:])
        else:print(a[6:])
    else:
        cs = fUz(a)
        try:cses[cs[0]] = cs[1]
        except Exception:pass
        return num(a)
        #returh(a)
