import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt

import mplcyberpunk

plt.style.use("cyberpunk")

def plow():
    mplcyberpunk.add_glow_effects()
    mplcyberpunk.add_underglow()


plt.how=plt.show

def show():
    plow()
    plt.how()
plt.show=show



