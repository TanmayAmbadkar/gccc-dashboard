from django import forms
from ranklist.models import *

class CollegeForm(forms.ModelForm):

    class Meta():
        model = College
        fields = ['short_name', 'long_name', 'description', 'email', 'csv', ]

        widgets = {
            'description' : forms.Textarea(),
        }
