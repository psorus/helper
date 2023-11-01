import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt

import mplcyberpunk
import scienceplots


import sys

punky=True
if len(sys.argv)>1:
    if "-ser" in sys.argv:
        punky=False
        sys.argv.remove("-ser")
    if "-serious" in sys.argv:
        punky=False
        sys.argv.remove("-serious")
classy=False
if len(sys.argv)>1:
    if "-cla" in sys.argv:
        classy=False
        sys.argv.remove("-cla")
    if "-classy" in sys.argv:
        punky=False
        sys.argv.remove("-classy")
   
if punky:
    plt.style.use("cyberpunk")

    def plow():
        mplcyberpunk.add_glow_effects()
        mplcyberpunk.add_underglow()
    
    
    plt.how=plt.show
    
    def show(*args,**kwargs):
        plow()
        plt.how(*args,**kwargs)
    plt.show=show
elif classy:
    plt.style.use("grayscale")
    plt.how=plt.show
else:
    font = {'family' : 'normal',
        #'weight' : 'bold',
        'size'   : 22}
    matplotlib.rc('font', **font)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.style.use(['science','no-latex'])
    plt.how=plt.show

def quantlimx(x,alpha=0.01, inc=0.0):
    import numpy as np
    xmin=np.quantile(x,alpha)
    xmax=np.quantile(x,1-alpha)
    if inc>0:
        delta=xmax-xmin
        xmin-=inc*delta/2
        xmax+=inc*delta/2
    plt.xlim((xmin,xmax))
    return xmin,xmax

def quantlimy(y,alpha=0.01, inc=0.0):
    import numpy as np
    ymin=np.quantile(y,alpha)
    ymax=np.quantile(y,1-alpha)
    if inc>0:
        delta=ymax-ymin
        ymin-=inc*delta/2
        ymax+=inc*delta/2
    plt.ylim((ymin,ymax))
    return ymin,ymax

plt.xlimq=quantlimx
plt.ylimq=quantlimy
plt.quantlimx=quantlimx
plt.quantlimy=quantlimy


