from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
#from django.urls import path 
from datetime import datetime
from .forms import PatientForm,Reviewform 
from .models import Review,PatientSideEffect,Patient


#def index(request):
#   return render(request, 'reviewForm.html')

def reviewForm(request):
    #form = Reviewform()

    if request.method == 'POST': 
        formR = Reviewform(request.POST)
        if formR.is_valid() :
            Review =formR.save(commit=False)
            Review.drugName=formR.cleaned_data.get('drugName')
            Review.condition=formR.cleaned_data.get('condition')
            Review.review=formR.cleaned_data.get('review')
            Review.rating=formR.cleaned_data.get('rating')
            
            Review.save()
            formR.save_m2m()
            print('review created')

    else:
            formR = Reviewform()
    context = {'formR':formR}
    return render(request, 'reviewForm.html',context)

def patientForm(request):
    
    #P_form=PatientForm()
    if request.method == 'POST':
        P_form = PatientForm(request.POST)
        if P_form.is_valid():
            Patient =P_form.save(commit=False)
            Patient.birth_date=P_form.cleaned_data.get('drugName')
            Patient.numTel=P_form.cleaned_data.get('condition')
            Patient.gender=P_form.cleaned_data.get('review')
            Patient.med_history=P_form.cleaned_data.get('rating')
            Patient.Wilaya=P_form.cleaned_data.get('condition')
            Patient.poids=P_form.cleaned_data.get('review')
            Patient.taille=P_form.cleaned_data.get('rating')
            Patient.preg=P_form.cleaned_data.get('rating')
            
            Patient.save()
            P_form.save_m2m()
            print('patient created')
    else:
        P_form = PatientForm()
    
    context = {'P_form':P_form}

    return render(request,'PatientForm.html',context)