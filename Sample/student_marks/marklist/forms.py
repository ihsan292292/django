from django.forms import ModelForm
from marklist.models import Student

class stform(ModelForm):
    class Meta:
        model = Student
        fields =('roll_no','name','mark1','mark2','mark3','total_mark','avg_mark')
        #fields="__all__"
