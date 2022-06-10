from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
#from django.urls import path 
from datetime import datetime
from .forms import PatientForm,Reviewform,CreateUserForm
from .models import Review,PatientSideEffect,Patient


#def index(request):
#   return render(request, 'reviewForm.html')

def review(request):
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

def patient(request):
    
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



def profile(request):

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        profile_form = PatientForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            #user.save_m2m() #maybe this is the error

            profile = profile_form.save(commit=False)
            profile.user=user

            user.med_history = profile_form.cleaned_data.get('med_history')
            user.numTel = profile_form.cleaned_data.get('numTel')
            user.gender = profile_form.cleaned_data.get('gender')
            user.Wilaya = profile_form.cleaned_data.get('Wilaya')
            user.poids = profile_form.cleaned_data.get('poids')
            user.taille = profile_form.cleaned_data.get('taille')
            user.birth_date = profile_form.cleaned_data.get('birth_date')
            user.preg = profile_form.cleaned_data.get('preg')
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)

            print('user created')
            messages.add_message(request, messages.SUCCESS , "You have Registered successfully" )
            #return redirect('home:home')
    else:
        form=CreateUserForm()
        profile_form = PatientForm()
            
            
            
    context = {'form' : form, 'profile_form' : profile_form }
    return render(request, 'profile.html', context) 