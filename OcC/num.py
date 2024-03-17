def num(a):
    aop = ['//','*','-','+','^']
    for i in aop:
        if i in a and 'num' in a:
            c = a.find(i)
            d = a.find('num')
            jg = str(eval(a[d+3:]))
            return jg
