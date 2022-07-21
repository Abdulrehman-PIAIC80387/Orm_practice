from multiprocessing import context
from tkinter import W
from typing import Dict
from django.shortcuts import render
from .models import *
from django.db.models import Q, Sum ,Count,Max,Min
from datetime import datetime
from datetime import date
# Create your views here.

def dash(request):
    collumn = WORKER.objects.values('firstname_name')
    get_name = WORKER.objects.get(firstname_name__icontains='rehman')
    user = WORKER.objects.filter(salary__gte=1000,department__icontains="sialkot")
    get_gmail = WORKER.objects.filter(mailing__contains='@gmail')
    get_city = WORKER.objects.filter(Q(department__icontains='sialkot') | Q(department__icontains='karachi'))
    get_salary_by_city = WORKER.objects.filter(department__icontains="sialkot").aggregate(Sum('salary'))['salary__sum'] or 0.00 
    count_hiring_by_year = WORKER.objects.filter(joining_date__year='2022').aggregate(Count('salary'))['salary__count'] or 0.00 
    spelling_collumn = WORKER.objects.values('firstname_name')
    got_list= list(spelling_collumn)
    got_name = got_list[0]['firstname_name']
    print(type(got_name))
    get_emplyee_by_id_city = WORKER.objects.filter(worker_id__gte=5,department__icontains="lahore")
    alpha= got_name[2:3]
    today = datetime.today()
    print(today)
    month = today.month
    year = today.year
    
    get_record_added_month = WORKER.objects.filter(joining_date__month=month)
    get_record_added_day = WORKER.objects.filter(joining_date__startswith=date.today())
    get_record_added_year = WORKER.objects.filter(joining_date__year=year)
    current_week = date.today().isocalendar()[1] 
    week = WORKER.objects.filter(joining_date__week=current_week)
    startdate= "2020-08-06" 
    endate = "2021-07-21"
    daterange = WORKER.objects.filter(joining_date__range=[startdate, endate])
    count_sumofsalary_by_month = WORKER.objects.filter(joining_date__month='7').aggregate(Count('salary'))['salary__count'] or 0.00 
    byCurrentdatemonth= WORKER.objects.filter(joining_date__year__range=[2019,2024]
                              ).aggregate(Count('salary'))['salary__count'] or 0.00 

    SumByDateRangeYear= WORKER.objects.filter(joining_date__year__range=[2019,2024]
                              ).aggregate(Sum('salary'))['salary__sum'] or 0.00 

    maxSalaryEmployee= WORKER.objects.aggregate(Max('salary'))['salary__max'] or 0.00 
    get_employee_name = WORKER.objects.filter(salary=maxSalaryEmployee)



    context={

        'collumn':collumn,





        'get_name':get_name,

        'user':user,
        'get_gmail':get_gmail,
        'get_city':get_city,
        'get_salary_by_city':get_salary_by_city,
        'count_hiring_by_year':count_hiring_by_year,
        'alpha':alpha,
        'get_emplyee_by_id_city':get_emplyee_by_id_city,
        'get_record_added_month':get_record_added_month,
        'get_record_added_day':get_record_added_day,
        'week':week,
        'daterange':daterange,
        'count_sumofsalary_by_month':count_sumofsalary_by_month,
        'byCurrentdatemonth':byCurrentdatemonth,
        'SumByDateRangeYear':SumByDateRangeYear,
        'get_employee_name':get_employee_name,
    }
   
    print(get_employee_name)

    return render(request, "base.html",context)

    