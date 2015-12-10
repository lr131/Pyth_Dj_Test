from django import forms
from django.forms import ModelForm, CharField
from .models import Student
<<<<<<< HEAD
from grups.models import Grup

#class StudForm(forms.ModelForm):
    #class Meta:
        #model = Student
        #fields = ('fio', 'bdata', 'bilet', 'cgrup')
        
class StudForm(forms.ModelForm):
    class Meta:
      model = Student
      fields = ('fio', 'bdata', 'bilet', 'cgrup')
    fio = forms.CharField(max_length=500, help_text='500 characters max.')
    bdata = forms.DateField(input_formats=['%d.%m.%Y'])
    bilet = forms.CharField(max_length=50)
    cgrup = forms.ModelChoiceField(queryset=Grup.objects.all())
=======

class StudForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fio', 'bdata', 'bilet', 'cgrup')
>>>>>>> ee4c7cb82f33d7200010c5481ed845302a09ee56
