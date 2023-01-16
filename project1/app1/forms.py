from django import forms
from .models import Mymodel

class MyForm(forms.ModelForm):
    class Meta:
        model=Mymodel
        fields='__all__'
