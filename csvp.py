import csv
import os
from contextlib import contextmanager



def read(fn,delimiter=",",quotechar='"',find_numbers=True,trafo=None):
    if trafo is None:trafo=lambda x:x 
    with open(fn,"r") as f:
        def denumber(q):
            try:
                return int(q)
            except:
                pass
            try:
                return float(q)
            except:
                pass
            return q
        def cleanup(q):
            q=q.strip()
            if len(q)>1:
                if q[0]==quotechar and q[-1]==quotechar:
                    q=q[1:-1]
            if find_numbers:
                return denumber(q)
            return q


        def readline():
            base=f.readline()
            if len(base)==0:return []
            base=base.strip()
            base=trafo(base)

            for row in csv.reader([base],delimiter=delimiter,quotechar=quotechar):
                return [cleanup(zw) for zw in row]

        header=readline()
        while True:
            ac=readline()
            if len(ac)==0:break

            yield {h:v for h,v in zip(header,ac)}
        
@contextmanager
def write(fn,keys,modus="a",delimiter=","):
    shallw=True
    if "a" in modus:shallw=not os.path.isfile(fn)
    with open(fn,modus) as f:
        if shallw:
            f.write(delimiter.join([str(zw) for zw in keys])+"\n")
        def oneline(q):
            f.write(delimiter.join([str(q[key]) for key in keys])+"\n")
        yield oneline



