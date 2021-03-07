import csv


def read(fn,*args,**kwargs):
    with open(fn,"r") as f:
        nam=None
        ret=[]
        for row in csv.reader(f,*args,**kwargs):
            if nam is None:
                nam=row
            else:
                ret.append({a:b for a,b in zip(nam,row)})
        return ret


def findfloats(q):
    if type(q) is list:return [findfloats(zw) for zw in q]
    if type(q) is dict:return {a:findfloats(b) for a,b in q.items()}
    try:
        return float(q)
    except:
        return q
