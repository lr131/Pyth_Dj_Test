from django.shortcuts import render
from .models import Student
from django.shortcuts import get_object_or_404
from grups.models import Grup


def student_edit(request, grup_id, st_id):
    gr_list = Grup.objects.order_by('name')
    stud_id = get_object_or_404(Student, pk=st_id)
    context = {'gr_id': grup_id, 'gr_list': gr_list, 'stud_id': stud_id}
    return render(request, 'students/student_edit.html', context)

def student_create(request, grup_id):
    gr_list = Grup.objects.order_by('name')
    context = {'gr_id': grup_id, 'gr_list': gr_list}
    return render(request, 'students/student_create.html', context)

