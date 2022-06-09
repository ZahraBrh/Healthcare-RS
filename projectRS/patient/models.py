from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import os

# Create your models here.
class Patient(models.Model):  
    GENDER=(
            ('Male','Male '),
            ('Female','Female '),
            )
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    numTel=models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=10,blank=False,choices=GENDER,default='male ')
    med_history = models.TextField(max_length=800, blank=True)
    Wilaya = models.CharField(max_length=30, blank=True)
    poids = models.IntegerField(null=False,blank=False)
    taille = models.IntegerField(null=False,blank=False)
    preg = models.BooleanField(null=False,blank=False, default=0)

    def __str__(self):
        return self.user.username 

class ListDrug(models.Model):
    drugName = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.drugName


class ListCondition(models.Model):
    condition = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.condition

class ListSideEffect(models.Model):
    SideEff = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.condition


class PatientSideEffect(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    drugName = models.ForeignKey(
        ListDrug, blank=True, null=True, on_delete=models.CASCADE)
    condition = models.ForeignKey(
        ListCondition, blank=True, null=True, on_delete=models.CASCADE)
    SideEff = models.ForeignKey(
        ListSideEffect, blank=True, null=True, on_delete=models.CASCADE)
    dateDebut = models.DateField()
    datefin = models.DateField()
    Evolution = models.CharField(max_length=50)
    Description = models.CharField(max_length=8000)
    otherDrug = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=True)
    #incr = models.IntegerField(default=1)

    def __str__(self):
        return '%s %s %s' % (self.user ,self.drugName, self.SideEff)





class Review(models.Model):

    Rating=((1,'1'),(2,'1'),(3,'3'),(4,'4'),(5,'5'))
    

    drugName = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    review = models.CharField(max_length=500)
    rating = models.IntegerField(blank=False,choices=Rating,default="3")
    #rating = models.IntegerField(blank=False,default="3")
    date = models.DateField(auto_now=False, auto_now_add=True)
    usefulCount = models.IntegerField(default=0)
    def __str__(self):
        return self.drugName




class SideEffect(models.Model):

    drugName = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    se = models.CharField(max_length=50)
    freq = models.DecimalField(max_digits = 5,decimal_places = 2)
    incr = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.drugName, self.condition)




