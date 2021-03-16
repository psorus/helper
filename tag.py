import os
import json

import sys
import numpy as np

posend=[".mp4",".avi"]
neverinv=[".txt"]

showinvalids=True


def valid(q):
    q=q.lower()
    for zw in posend:
        if zw in q:return True
    for zw in neverinv:
        if zw in q:return False
    if showinvalids:print("found invalid file",q)
    return False

def listfiles(q):
    #print("listing in",q)
    ret=[]
    for zw in os.listdir(q):
        if os.path.isdir(q+"/"+zw):
            for zx in listfiles(q+"/"+zw):ret.append(zx)
            continue    
        if not valid(zw):continue   
        ret.append(q+"/"+zw)
    #print(ret)
    return ret

def hasconf(folder):
    return os.path.isfile(folder+"/conf.txt")
def loadconf(folder):
    if not hasconf(folder):return {}
    with open(folder+"/conf.txt","r") as f:
        return json.loads(f.read())
def saveconf(folder,data):
    with open(folder+"/conf.txt","w") as f:
        f.write(json.dumps(data,indent=2))



def recursiveconf(folder):
    print("reccuring on",folder)
    ret={}
    if hasconf(folder):
        for key,val in loadconf(folder).items():ret[key]=val
    for zw in os.listdir(folder):
        zw=folder+"/"+zw
        if os.path.isfile(zw):continue
        for key,val in recursiveconf(zw).items():
            key=(zw+"/"+key).replace("////","//")
            if key in ret.keys():
                for zx in val:
                    ret[key].append(zx)
                ret[key]=list(set(ret[key]))
            else:
                ret[key]=val
    return ret



def form(q):
    return q.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")

def mainloop(q,shallopen=True):
    if shallopen:print("opening",q)
    #return ""
    if shallopen:os.system("vlc "+form(q)+"&")
    ret=[]
    while True:
        ac=input("Please enter one tag. keep empty to stop this loop\n")
        if len(ac)==0:break
        ret.append(ac)
    print("the current tags are",*ret)
    ok="q"
    while ok!="y" and ok!="n":
        ok=input("Are you happy with this? (y/n)")
    if ok=="n":return mainloop(q,shallopen=False)
    return ret


def workon(folder="."):
    files=listfiles(folder)

    #exit()

    print("found",len(files),"files")

    if hasconf(folder):
        print("Found existing config file")
    else:
        print("Did not find any config file, creating it")

    q=recursiveconf(folder)
    print("This file(or its children) contain",len(q),"Elements")

    #print(files)
    
    np.random.shuffle(files)


    for fil in files:
        if fil in q.keys():continue
        q[fil]=mainloop(fil)
        saveconf(folder,q)



if __name__=="__main__":

    folder="/home/psorus/M/"
    if len(sys.argv)>1:
        folder=sys.argv[1]


    workon(folder)




