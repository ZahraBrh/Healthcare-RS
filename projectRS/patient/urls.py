from django.urls import path
from . import views

urlpatterns = [
   #path('', views.index, name='index'),
    path('review', views.reviewForm, name='reviewform'),
    path('', views.patientForm, name='Patientform'),
]