#find locations in which a function is below a certain threshold to plot them nicely
import numpy as np


def quickmin(x, y, border=None):
    if border is None:
        border = np.min(y)*0.95+np.max(y)*0.05
    pos=np.where(y<border)[0]

    last=-3
    inregion=False
    regionstart=0
    regionend=0
    regions=[]
    for i,p in enumerate(pos):
        if inregion:
            if p==last+1:
                #continue region
                regionend=p
            else:
                #end region
                regions.append([regionstart,regionend])
                inregion=False
        else:
            inregion=True
            regionstart=p
            regionend=p
        last=p
    if inregion:
        regions.append([regionstart,regionend])
    regx=[[x[zw] for zw in range(z[0],z[1]+1)] for z in regions]
    #return [[zw[0],zw[-1]] for zw in regx]
    regy=[[y[zw] for zw in range(z[0],z[1]+1)] for z in regions]
    regdex=[np.argmin(zw) for zw in regy]
    ret=[zw[dex] for zw,dex in zip(regx,regdex)]
    return ret

def quickmax(x, y, border):
    return quickmin(x, -y, -border)

if __name__=="__main__":
    from plt import plt
    x=np.arange(0,30,0.10)
    y=np.sin(x)
    points=quickmin(x,y,-0.9)
    plt.plot(x,y,"o",alpha=0.4)
    for point in points:
        try:
            plt.axvspan(point[0],point[1],alpha=0.5,color='r')
        except:
            plt.axvline(x=point,color='r')
    plt.show()



