from django.core.exceptions import ValidationError
from django import forms

from .models import *

class StudentForm(forms.Form):
    name = forms.CharField(label="Name")
    gender = forms.ChoiceField(choices=(('MALE','Male'),('FEMALE','Female')))
    senior = forms.NullBooleanField()
    num_of_books = forms.IntegerField()

def clean_num_of_books(self):
    value = self.cleaned_data.get('num_of_books')
    if not value<5 and not value>0:
        raise ValidationError(("Number of books is not valid!"), code='invalid')
    return value

class BookForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    genre = forms.CharField(max_length=25,)
    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all())             # MtO
    pages = forms.IntegerField()

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'        

class RecordForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())                   # FK
    book = forms.ModelChoiceField(queryset=Book.objects.all())                         # FK
    took_date = forms.DateField()
    returned_date = forms.DateField()
    returned = forms.BooleanField()