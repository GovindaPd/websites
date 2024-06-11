from dateutil import relativedelta
from datetime import datetime

def inyears(todate,fromdate,totaldays):
    r = relativedelta.relativedelta(todate,fromdate)
    if r.days >= 7:
        week = int(r.days/7)
        if r.days%7 == 0 :
            rdays = 0
        else :
            rdays = r.days%7
    else:
        rdays = r.days
        week = 0
    iny = "In Years : "+str(r.years)+" Years "+str(r.months)+" Months "+str(week)+" Weeks "+str(rdays)+" Days"

    inmonth = r.years*12 + r.months
    inm = "In Months : "+str(inmonth)+" Months "+str(week)+" Weeks "+str(rdays)+" Days"
    return iny,inm

def inweeks(days):
    totalweek = int(days/7)
    if days%7 == 0 :
        inw = "In Weeks : "+str(totalweek)+" Weeks 0 Days"
    else :
        rdays = days%7
        inw = "In Weeks : "+str(totalweek)+" Weeks "+str(rdays)+" Days"
    return inw
def indays(days):
    ind = "In Days : "+str(days)+" Days"
    return ind
def inhours(days):
    totalhour = days*24
    inh = "In Hours : "+str(totalhour)+" Hours"
    return inh
def inminutes(days):
    totalminute = days*24*60
    inmi = "In Minutes : "+str(totalminute)+" Minutes"
    return inmi
def inseconds(days):
    totalsecond = days*24*60*60
    ins = "In Seconds : "+str(totalsecond)+" Seconds"
    return ins

def nextbrithday(fromdate,todate):
    wish = ""
    dd1 = datetime(todate.year,fromdate.month,fromdate.day)
    dd2 = datetime(todate.year+1,fromdate.month,fromdate.day)
    if fromdate.month>todate.month:
        rd = dd1
    if fromdate.month<todate.month:
        rd = dd2
    if fromdate.month == todate.month:
        if fromdate.day > todate.day:
            rd = dd1
        if fromdate.day < todate.day:
            rd = dd2
        if fromdate.day == todate.day:
            rd = dd2
            wish = "👏👏🕯️🎉 Happy Birthday To You 🎂 🍾🍾🎁 And Your "
    rrd = rd-todate
    nb = wish+"Next Birthday In : "+str(rrd.days)+" Days"
    return nb

def extrainfo(totaldays):
    rl = []
    #heart beats around 80 time per minutes 
    heart = totaldays*115200
    rl.append("Your Heart Has Beaten Around : "+str(heart) + " Times")
    #breath 200000 per 
    breath = totaldays*20000
    rl.append("You Have Taken Breaths Around : "+str(breath))
    #lough 20 times per days*20
    laugh = totaldays*20 
    rl.append("You Have Laughed Around : "+str(laugh) + " Times")
    #sleep in a day 8 hours so in days 1 day = 0.334
    sleep = round(totaldays*0.334)
    rl.append("You Have Slept Around : "+str(sleep) + " Days")
    #walk 2 miles per day 
    walk = totaldays*2
    rl.append("You Have Walked Around : "+str(walk) + " Miles")
    #ton of eats 4 pound per day so in tons 0.00181437*days
    food = round(totaldays*0.00181437)
    rl.append("You Have Eaten Around : "+str(food) + " Tons Of Food")
    #eating and dinking per day 1hour 8 minute so in day 1 day = 0.04723
    eat_an_drink = round(totaldays*0.04723)
    rl.append("You Have Spent Time For Eating & Drinking Around : "+str(eat_an_drink) + " Days")
    return rl
