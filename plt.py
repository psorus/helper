import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt

import mplcyberpunk

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
    plt.style.use(['science','no-latex'])
    plt.how=plt.show


