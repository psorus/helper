import numpy as np

from graham import findorthogonal


def cov(a,b):
    return ((len(a)-1)/(len(a)))*np.mean([aa*bb for aa,bb in zip(a,b)])

class dataset(object):
    def __init__(s,q):
        s.q=q
    def __len__(s):
        return len(s.q)
    def __add__(a,b):
        return a.__class__([aa+bb for aa,bb in zip(a.q,b.q)])
    def __sub__(a,b):
        return a.__class__([aa-bb for aa,bb in zip(a.q,b.q)])
    def scalar(a,b):
        return cov(a.q,b.q)
    def multwithfloat(s,a):
        return s.__class__([aa*a for aa in s.q])
    def __mul__(a,b):
        if type(a) is int or type(a) is float:
            return b.multwithfloat(a)
        if type(b) is int or type(b) is float:
            return a.multwithfloat(b)
        return a.scalar(b)
    def __rmul__(a,b):
        if type(a) is int or type(a) is float:
            return b.multwithfloat(a)
        if type(b) is int or type(b) is float:
            return a.multwithfloat(b)
        return a.scalar(b)

def decor(x):
    dim=int(x.shape[1])
    ds=[dataset(x[:,i]) for i in range(dim)]
    o=findorthogonal(*ds)
    o=[np.expand_dims(oo.q,1) for oo in o]
    o=np.concatenate(o,axis=1)
    return o














if __name__ == '__main__':
    x=np.random.normal(0,1,(1000,3))
    x[:,0]+=x[:,1]

    print(np.corrcoef(x.T))

    y=decor(x)

    print(np.corrcoef(y.T))








