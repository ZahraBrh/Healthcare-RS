from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
#from django.urls import path 
from datetime import datetime
from .forms import Reviewform
from .models import Review


#def index(request):
#   return render(request, 'reviewForm.html')

def reviewForm(request):
    form = Reviewform()
    if request.method == 'POST': 
        form = Reviewform(request.POST,request.FILE)
        if form.is_valid() :
            Review =form.save(commit=False)
            Review.drugName=form.cleaned_data.get('drugName')
            Review.condition=form.cleaned_data.get('condition')
            Review.review=form.cleaned_data.get('review')
            Review.rating=form.cleaned_data.get('rating')
            Review.save()
            form.save_m2m()
            print('post created')
        else:
            form = Reviewform()
    context = {'form':form}
    return render(request, 'reviewForm.html',context)