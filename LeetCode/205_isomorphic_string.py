s = 'babc'
t = 'baba'

def isomorphic_string(s, t):
    d = {}
    if len(s) != len(t): return False

    for sitem, titem in zip(s, t):
        # print(d)
        # print(sitem, titem)
        if sitem in d.keys() and d[sitem] != titem:
            return False
        else:
            d[sitem] = titem

          
    if len((set(d.keys()))) == len(set(d.values())):
        return True
    else:
        return False


print(isomorphic_string(s, t))
 
