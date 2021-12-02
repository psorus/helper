import numpy as np
import matplotlib.pyplot as plt

def coroplot(mat,lab=None,fs=14):
    mat=[[0 if np.isnan(zx) else zx for zx in z] for z in mat]
    if lab is None:
        lab=[str(i+1) for i in range(len(mat))]

    plt.imshow(np.abs(mat), cmap='binary')
    plt.clim(0,1)

    for i1,v in enumerate(mat):
        for i2,val in enumerate(v):
            if abs(val)>0.5:
                col=1.0
            else:
                col=0.0
            col=[col,col,col]
            if val<0:
                col=[1.0,0.0,0.0]
            plt.text(i1,i2,str(round(val,4)),va="center",ha="center",fontsize=fs,color=col)



    plt.yticks(np.arange(len(mat)), lab)
    plt.xticks(np.arange(len(mat)), lab)


    ax=plt.gca()

    ax.xaxis.tick_top()
    
    plt.colorbar()



