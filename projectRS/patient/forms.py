from django import forms
from .models import Review
from django.forms import ModelForm
from datetime import date

class Reviewform(forms.ModelForm): 
    class Meta:
        model = Review
        fields = [
            "drugName","condition","review","rating",
        ]
        labels = {
            "drugName":"Drug Name",
            "condition":"condition",
            "review":"review",
            "rating":"rating",
            "usefulCount":"usefulCount",
        }
        widgets = {
            "drugName":forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'Insert Drug Name'}),
            "condition":forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'In Drug Name.'}),
            "review":forms.Textarea(attrs={'class':'form-control',
                                    'placeholder':'review...'}),   
            'rating':forms.Select(attrs={'class':'form-control',
                                    'placeholder':'Select your domaine interest...'}),
                    }