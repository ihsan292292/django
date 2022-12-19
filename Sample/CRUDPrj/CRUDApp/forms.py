from django import forms
from django.forms import ModelForm, models

from .models import Stud


class stform(ModelForm):
    class Meta:
        model = Stud
        fields =('sname','sadds','scity','semail','sphon')
        #fields="__all__"
