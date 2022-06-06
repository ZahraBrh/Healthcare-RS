from django.db import models
from django.utils import timezone

# Create your models here.


class Patient(models.Model):

    GENDER=(
            ('Male','Male '),
            ('Female','Female '),
            )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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


class Review(models.Model):
    Rating=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    
    drugName = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    review = models.CharField(max_length=500)
    rating = models.IntegerField(blank=False,choices=Rating)
    date = models.DateField(auto_now=False, auto_now_add=True)
    usefulCount = models.IntegerField(default=0)

    def __str__(self):
        return self.drugName





class PatientSideEffect(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    drugName = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    se = models.CharField(max_length=50)
    freq = models.DecimalField(max_digits = 5,decimal_places = 2)
    
    date = models.DateField(auto_now=False, auto_now_add=True)
    incr = models.IntegerField(default=1)


class SideEffect(models.Model):
    drugName = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    se = models.CharField(max_length=50)
    freq = models.DecimalField(max_digits = 5,decimal_places = 2)
    incr = models.IntegerField(default=0)







