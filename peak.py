import numpy as np
import sys
from simplestat import sprint, statinf




f=None
ac=None

def peak(fn):
    print(f"peaking {fn}")
    global f
    global ac
    f=np.load(fn)
    #print(f.files)
    for fil in f.files:
        ac=f[fil]
        print(fil,ac.shape)
        if np.prod(ac.shape)<=10:
            print(ac)
    print("")




if __name__ == '__main__':
    if len(sys.argv)>1:
        for fn in sys.argv[1:]:
            peak(fn)
    else:
        #peak("../../data.npz")#debug
        print("Usage: peak.py <file1> <file2> ...")
