from priht import priht
#from lf import lf
from fuz import fUz
from num import num

def cha(a):
    c = []
    try:
        b = open(fr'{a}','r')
        while 1:
            txt = b.readline()
            if txt:
                c.append()
            else:
                for i in c:
                    priht(i)
    except Exception:
        priht(a)
