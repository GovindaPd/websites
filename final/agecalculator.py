from flask import render_template, request, redirect, Blueprint
from datetime import datetime
from agecalculator_logic import inyears, inweeks, indays, inhours, inminutes, inseconds, nextbrithday, extrainfo
import content
from utility_function import getcontext


agecalculator = Blueprint('agecalculator', __name__)

currentdate = datetime.today()
    

@agecalculator.route('/')
def home():
    context = getcontext()
    context['byear'] = 1900
    context['bmonth'] = 1
    context['bday'] = 1
    context['cyear'] = currentdate.year
    context['cmonth'] = currentdate.month
    context['cday'] = currentdate.day
    return render_template('agecalculator.html', context=context)

@agecalculator.route('/calculate_age_result', methods=['GET','POST'])
def calculate_age_result():
    mylist = []
    if request.method == 'POST':
        context = getcontext()
        try:
            byear = int(request.form['fromyear'])
            bmonth = int(request.form['frommonth'])
            bday = int(request.form['fromday'])
            cyear = int(request.form['toyear'])
            cmonth = int(request.form['tomonth'])
            cday = int(request.form['today'])
        except TypeError as error:
            return redirect(url_for('agecalculator.home'))

        context['byear'] = byear
        context['bmonth'] = bmonth
        context['bday'] = bday
        context['cyear'] = cyear
        context['cmonth'] = cmonth
        context['cday'] = cday

        fromdate = datetime(byear,bmonth,bday)
        todate = datetime(cyear,cmonth,cday)
        totaldays = todate - fromdate
        iny,inm = inyears(todate,fromdate,totaldays.days)
        mylist.append(iny)
        mylist.append(inm)
        inw = inweeks(totaldays.days)
        mylist.append(inw)
        ind = indays(totaldays.days)
        mylist.append(ind)
        inh = inhours(totaldays.days)
        mylist.append(inh)
        inmi = inminutes(totaldays.days)
        mylist.append(inmi)
        ins = inseconds(totaldays.days)
        mylist.append(ins)
        nb = nextbrithday(fromdate,todate)
        mylist.append(nb)

        context['extra'] = extrainfo(totaldays.days)
        
        return render_template('agecalculator.html',mylist=mylist, context=context)
    else:
        return redirect(url_for('agecalculator.home'))
