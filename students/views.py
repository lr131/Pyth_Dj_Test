from django.shortcuts import render
from django.shortcuts import redirect
from .forms import StudForm
from .models import Student
from django.shortcuts import get_object_or_404
from grups.models import Grup


def student_edit(request, grup_id, st_id):
    stud = get_object_or_404(Student, pk=st_id)
    if request.method == "POST":
        form = StudForm(request.POST, instance=stud)
        if form.is_valid():
            stud = form.save()
            stud.save()
            return redirect('grups.views.students_list', grup_id)
    else:
        form = StudForm(instance=stud)
    return render(request,'students/student_edit.html', {'form': form})


def student_create(request, grup_id):
    gr_id = get_object_or_404(Grup, pk=grup_id)
    if request.method == "POST":
        form = StudForm(request.POST)
        if form.is_valid():
            stud = form.save()
            return redirect('grups.views.students_list', grup_id)
    else:
      form = StudForm(initial={'cgrup': grup_id})
    return render(request, 'students/student_edit.html', {'form': form})
  

def student_del(request, grup_id, st_id):
    stud = get_object_or_404(Student, pk=st_id)
    try:
      stud.delete()
      return redirect('grups.views.students_list', grup_id)
    except Exception as e:
      form = StudForm(instance=stud)
      return render(request, 'students/student_edit.html', {'form': form, 'stud': stud, 'error_message': e})