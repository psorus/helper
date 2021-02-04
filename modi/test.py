from fuzzy import *
from time import time


n=int(1e6)


t0=time()
for i in range(n):
    ff=Fuzzy(0.1)
t1=time()


print(ff)
print((t1-t0)/n)

