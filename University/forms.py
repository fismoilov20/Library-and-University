from django import forms
from .models import *

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'