from django import forms
from django.forms import ModelForm, models

from .models import stud

class stform(ModelForm):
    class Meta:
        model = stud
        fields = ('sname','sadds','scity','semail','sphon')