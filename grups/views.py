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
    gr_id = get_object_or_404(Grup, pk=grup_id)
    context = {'gr_id': gr_id}
    return render(request, 'grups/students_list.html', context)

def grup_create(request):
#    context = {'gr_id': grup_id}
    context = {'gr_id': 0}
#    return render(request, 'grups/grup_create.html', context)
    return render(request, 'grups/form_gr.html')

def grup_edit(request, grup_id):
    gr_id = get_object_or_404(Grup, pk=grup_id)
    context = {'gr_id': gr_id}
#    return render(request, 'grups/grup_edit.html', context)
     return render(request, 'grups/form_gr.html', context)

