from django.urls import path
from .import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('review', views.review, name='reviewform'),
    #path('', views.patient name='Patientform'),
    path('', views.profile, name='Profiletform'),
]