from tqdm import tqdm


def uqdm(iterable,*args,**kwargs):
    t=tqdm(iterable,*args,**kwargs)
    def func(text,t=t):
        t.set_description_str(str(text))
    for zw in t:
        yield zw,func



if __name__=="__main__":
    import time

    for i,func in uqdm(range(100)):
        time.sleep(0.1)
        func(str(i))
        

