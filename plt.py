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
   
if punky:
    plt.style.use("cyberpunk")

    def plow():
        mplcyberpunk.add_glow_effects()
        mplcyberpunk.add_underglow()
    
    
    plt.how=plt.show
    
    def show():
        plow()
        plt.how()
    plt.show=show



