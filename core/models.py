from django.db import models
import datetime as datetime
from django.utils.timezone import now
# Create your models here.


class WORKER(models.Model):
    firstname_name = models.CharField('firstname_name', max_length=120, default='', blank=True, null=True)
    last_name = models.CharField('last_name', max_length=120, default='', blank=True, null=True)
    department = models.CharField('address', max_length=120, default='', blank=True, null=True)
    worker_id = models.IntegerField('worker_id', default=0, blank=True, null=True)
    salary = models.IntegerField('Salary', default=0, blank=True, null=True)
    joining_date = models.DateTimeField(auto_now_add=False, auto_now=False,null=True)
    mailing = models.EmailField(blank=True, null=True, default='')
   
    def __str__(self):
        return self.firstname_name or ''

    
class BONUS(models.Model):
   
    bonus_date = models.DateField(null=True)
    Bonus_id = models.IntegerField('Bonus_id ', default=0, blank=True, null=True)
    bonus_amount =  models.IntegerField('bonus_amount ', default=0, blank=True, null=True)


class Title(models.Model):
    worker_id = models.IntegerField('worker_id', default=0, blank=True, null=True)
    worker_title = models.CharField('person_name', max_length=120, default='', blank=True, null=True)
    affected_from = models.DateTimeField(auto_now_add=False, auto_now=False,null=True)
    