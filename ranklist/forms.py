from django import forms
from ranklist.models import *

class CollegeForm(forms.ModelForm):

    class Meta():
        model = College
        fields = '__all__'

        widgets = {
            'description' : forms.Textarea(),
        }
