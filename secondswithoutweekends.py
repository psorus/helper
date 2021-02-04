from datetime import datetime,timedelta

oneday=timedelta(days=1)

def isweekend(day):
    wd=day.weekday()
    return wd==5 or wd==6
def issaturday(day):
    wd=day.weekday()
    return wd==5
def issunday(day):
    wd=day.weekday()
    return wd==6


def ignore_everything_but_days(ac):
    return datetime(year=ac.year,month=ac.month,day=ac.day)

def nextsaturday(day):
    if isweekend(day):return day
    ac=ignore_everything_but_days(day)
    while not issaturday(ac):ac+=oneday
    return ac
    #return ignore_everything_but_days(ac)

def lastmonday(day):
    if isweekend(day):return day
    ac=ignore_everything_but_days(day)
    while not issunday(ac):ac-=oneday
    return ac
    #return ignore_everything_but_days(ac)

def tillweekend(day):
    return (nextweekend(day)-day).total_seconds()
def sinceweekend(day):
    return (day-lastweekend(day)).total_seconds()
def isweekendbetween(t0,t1):
    if (t1-t0).total_seconds()/86400>=7:return True
    ac=t0
    while ac<t1:
        if isweekend(ac):return True
        ac+=oneday
    return False
def timedelta_ignoringweekends(t0,t1):
    """calculates the total time between t0 and t1 (assuming t1 is later than t0) ignoring every weekend"""
    if (t1-t0).total_seconds()<0:return timedelta_ignoringweekends(t1,t0)
    if not isweekendbetween(t0,t1):
        return (t1-t0).total_seconds()
    #print("found a weekend")
    t0w=nextsaturday(t0)
    t1w=lastmonday(t1)
    #print(t0w,t1w)
    add0=(t0w-t0).total_seconds()
    add1=(t1-t1w).total_seconds()
    t0w=ignore_everything_but_days(t0w)
    t1w=ignore_everything_but_days(t1w)
    main=(t1w-t0w).total_seconds()*(5/7)
    #print("deltas",add0,add1,main)
    return main+add0+add1


if __name__=="__main__" and False:
    t0=datetime.now()
    t0=ignore_everything_but_days(t0)
    onehour=timedelta(hours=1)
    for i in range(24):
        ac=t0+onehour*i
        print(ac,ac.weekday())


if __name__=="__main__":
    t0=datetime.now()
    t0=ignore_everything_but_days(t0)
    print(t0,t0.weekday())
    t1=t0+50000*oneday
    t1=t0+500000*oneday
    print(t1,t1.weekday())
    delta=(timedelta_ignoringweekends(t0,t1))
    print(delta)
    print(delta/86400)
    print(delta/86400*7/5)
    #print(timedelta_ignoringweekends(t0,t1)/86400)

    exit()
    print(tillweekend(datetime.now()))
    print(sinceweekend(datetime.now()))
    print(tillweekend(datetime.now())+sinceweekend(datetime.now()))

