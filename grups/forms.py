from django import forms

from .models import Grup

class GrupForm(forms.ModelForm):
    class Meta:
        model = Grup
        fields = ('name', 'starosta')