#i think you could solve this by prime products (aka dual prime hypothesis)
#so lets do this

#not perf rnd
#could you use something like iterator of iterator for this
#in other words does x_i+1=x_i+zw%c where zw=[1,2,3,4,5,6] result in x_i==x_i, i!=j?



from modi import Modi as m
from modi import merge

primes=[1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]#....
#you should never need more than this, as this allows for prod(primes) elements (which would be 2305567963945518424753102147331756070)




def _repeatit(cou,moduli=1,init=0):#uses modulos here
    j=0
    i=m(init%cou,cou)#could use this 0 as a seeding point
    while True:
        yield i
        j+=1
        if not j%moduli:
            j=0
            i+=1

def multimerge(f):
    if len(f)==0:return m(0,1)
    ret=f[0]
    for zw in f[1:]:
        ret=merge(ret,zw)
    return ret

def _iternum(f,seed=0,includefirst=False):
    """f is a list of numbers that dont share factors. The iterator runs up to prod(f). includefirst: seed is the first value, !includefirst: seed is the last value"""
    it=[]
    mod=1
    for zw in f:
        it.append(_repeatit(zw,mod,seed))
        mod*=zw
    #it=[_repeatit(zw) for zw in f]
    pro=1
    for zw in f:pro*=zw
    if includefirst:
        for i in range(pro):
            ac=[zw.__next__() for zw in it]
            yield multimerge(ac).value
    else:
        for i in range(pro+1):
            ac=[zw.__next__() for zw in it]
            if i>0:yield multimerge(ac).value

def _itermaxnum(f,maxv,seed=0,includefirst=False):
    """_iternum, but cut out everything >=maxv"""
    it=_iternum(f,seed=seed,includefirst=includefirst)
    for zw in it:
        if zw>=maxv:continue
        yield zw

def random_iterate(maxv,seed=0,includefirst=False):
    """"""
    modulo=1
    f=[]
    for p in primes:
        f.append(p)
        modulo*=p
        if modulo>maxv:break#below or same, to reduce predictability for the price of speed. Main difference to random_iterate_faster
        
    for zw in _itermaxnum(f,maxv,seed=seed,includefirst=includefirst):
        yield zw

def random_iterate_faster(maxv,seed=0,includefirst=False):
    """same as random_iterate, but sligthly faster and sligthly more predictable"""
    modulo=1
    f=[]
    for p in primes:
        f.append(p)
        modulo*=p
        if modulo>=maxv:break
        
    for zw in _itermaxnum(f,maxv,seed=seed,includefirst=includefirst):
        yield zw


if __name__=="__main__":
    tes=[]
    for zw in random_iterate(50):#_iternum([2,3,5],12):
        print(zw)
        tes.append(zw)
    print(len(tes),len(set(tes)))
    #speedtest
    from time import time as t
    n=10000
    t0=t()
    it=random_iterate(1000_000_0)
    for i in range(n):
        ac=it.__next__()
    t1=t()
    print(n,t1-t0)







