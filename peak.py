import numpy as np
import sys


def peak(fn):
    print(f"peaking {fn}")
    f=np.load(fn)
    print(f.files)
    print("")




if __name__ == '__main__':
    if len(sys.argv)>1:
        for fn in sys.argv[1:]:
            peak(fn)
    else:
        #peak("../../data.npz")#debug
        print("Usage: peak.py <file1> <file2> ...")









