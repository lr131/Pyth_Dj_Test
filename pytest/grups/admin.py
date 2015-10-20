from django.contrib import admin
from django.forms import ModelForm
from .models import Grup
from students.models import Student


class GrupAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GrupAdminForm, self).__init__(*args, **kwargs)
        self.fields['starosta'].queryset = Student.objects.filter(cgrup = self.instance.id)
        
        

class StudentInline(admin.TabularInline):
    model = Student
    extra = 5

class GrupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    form = GrupAdminForm
    list_display = ('name', 'starosta')
    
admin.site.register(Grup, GrupAdmin)
