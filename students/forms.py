from django import forms
from django.forms import ModelForm, CharField
from .models import Student

class StudForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fio', 'bdata', 'bilet', 'cgrup')