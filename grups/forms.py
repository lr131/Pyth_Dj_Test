from django import forms
from students.models import Student
from .models import Grup

class GrupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GrupForm, self).__init__(*args, **kwargs)
        self.fields['starosta'].queryset = Student.objects.filter(cgrup=self.instance.id)
        for name in self.fields:
            self.fields[name].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Grup
        fields = ('name', 'starosta')