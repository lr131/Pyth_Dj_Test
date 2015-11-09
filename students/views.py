from django.shortcuts import render
from .models import Student
from grups.models import Grup



# Create your views here.
def students_list(request, grup_id):
    st_list = Student.objects.order_by('fio')
#gr_list = Grup.objects.filter(pk=Student.cgrup)

    gr_list = Grup.objects.filter(pk=grup_id)
    context = {'st_list': st_list, 'gr_list': gr_list, 'grup_id': grup_id}
    return render(request, 'grups/students_list.html', context)
