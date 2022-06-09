from django import forms
from .models import Review,Patient,SideEffect
from django.forms import ModelForm
from datetime import date
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView,UpdateView,DeleteView


class CreateUserForm(UserCreationForm):
        email = forms.EmailField(required=True, help_text='Required.',widget=forms.EmailInput(attrs={'class':'form-control',
                        'placeholder':'Email...'}))
        first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                            'placeholder':'First name...'}))
        last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                            'placeholder':'Last name...'}))
        username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                            'placeholder':'Username...'}))
        class Meta:
            model = User
            fields = ['username','first_name','last_name','email','password1','password2',]
            
        def save(self,commit=True):
            user=super().save(commit=False)

            user.email=self.cleaned_data['email']
            user.first_name=self.cleaned_data['first_name']
            user.last_name=self.cleaned_data['last_name']

            if commit: 
                user.save()
            return user    


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['birth_date','numTel','gender','med_history','Wilaya','poids','taille','preg',
                    ]
        labels = {
            'med_history':'antecedent',
            'preg':'grossesse',
                }
                                        
        widgets = {            
                        'med_history':forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'Historique médicale, antécédant ...'}),
                        'gender':forms.Select(attrs={'class':'form-control',
                                    'placeholder':'gender ...'}),
                        'Wilaya':forms.Select(attrs={'class':'form-control',
                                    'placeholder':'Selectionner votre Wilaya...'}),
                        'birth_date':forms.TextInput(attrs={'class':'form-control',
                                    'placeholder':'YYYY-MM-DD.'}),
                    }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField( widget=forms.PasswordInput)

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
                    }