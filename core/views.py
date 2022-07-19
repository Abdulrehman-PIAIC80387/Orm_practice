from multiprocessing import context
from tkinter import W
from typing import Dict
from django.shortcuts import render
from .models import *
from django.db.models import Q, Sum ,Count
# Create your views here.

def dash(request):
    collumn = WORKER.objects.values('firstname_name')
    get_name = WORKER.objects.get(firstname_name__icontains='rehman')
    user = WORKER.objects.filter(salary__gte=1000,department__icontains="sialkot")
    get_gmail = WORKER.objects.filter(mailing__contains='@gmail')
    get_city = WORKER.objects.filter(Q(department__icontains='sialkot') | Q(department__icontains='karachi'))
    get_salary_by_city = WORKER.objects.filter(department__icontains="sialkot").aggregate(Sum('salary'))['salary__sum'] or 0.00 
    count_hiring_by_year = WORKER.objects.filter(joining_date__year='2022').aggregate(Count('salary'))['salary__count'] or 0.00 
    context={

        'collumn':collumn,
        'get_name':get_name,
        'user':user,
        'get_gmail':get_gmail,
        'get_city':get_city,
        'get_salary_by_city':get_salary_by_city,
        'count_hiring_by_year':count_hiring_by_year,
    }
    print(count_hiring_by_year)
    return render(request, "base.html",context)