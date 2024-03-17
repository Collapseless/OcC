from num import num

def fUz(z):
    c = z.find('=')
    if c != -1:
        return [z[0:c],z[c+1:]]
    #return num(z)
