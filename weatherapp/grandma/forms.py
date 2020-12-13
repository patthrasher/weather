from django import forms
from .models import Weather

class Weather_form(forms.ModelForm) :
    class Meta :
        model = Weather
        fields = ['city']

# class details_form(forms.ModelForm) :
#     class Meta :
