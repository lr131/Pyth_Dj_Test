from django.shortcuts import render
from students.models import Student
from django.shortcuts import get_object_or_404
from .models import Grup


# Create your views here.
def grups_list(request):
    gr_list = Grup.objects.order_by('name')
    context = {'gr_list': gr_list}
    return render(request, 'grups/grups_list.html', context)

def students_list(request, grup_id):
#    st_list = Student.objects.order_by('fio')
    gr_id = get_object_or_404(Grup, pk=grup_id)
    context = {'gr_id': gr_id}
    return render(request, 'grups/students_list.html', context)
