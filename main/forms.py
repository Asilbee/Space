from django import forms
from main.models import *

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email()
        fields = '__all__'
