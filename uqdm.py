from tqdm import tqdm
import numpy as np

def uqdm(iterable,rounde=4,*args,**kwargs):
    t=tqdm(iterable,*args,**kwargs)
    def func(text,rounde=rounde,t=t):
        if type(text) is float or type(text) is np.float64:
            text=round(text,rounde)
            prekomma,postkomma=str(text).split('.')
            while len(postkomma)<rounde:
                postkomma+='0'
            text=prekomma+'.'+postkomma
        t.set_description_str(str(text))
    for zw in t:
        yield zw,func



if __name__=="__main__":
    import time

    for i,func in uqdm(range(100)):
        time.sleep(0.1)
        func(1/(i+1))
        

