from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from students.models import Student
from .models import Grup
from .forms import GrupForm


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
    if request.method == "POST":
        form = GrupForm(request.POST)
        if form.is_valid():
            form.save()
            #grup = form.save()
            #grup.save()
            return redirect('grups.views.grups_list')
    else:
        form = GrupForm()
    return render(request, 'grups/grup_edit.html', {'form': form})


def grup_edit(request, grup_id):
    grup = get_object_or_404(Grup, pk=grup_id)
    if request.method == "POST":
        form = GrupForm(request.POST, instance=grup)
        if form.is_valid():
            grup = form.save()
            grup.save()
            return redirect('grups.views.grups_list')
    else:
        form = GrupForm(instance=grup)
    return render(request, 'grups/grup_edit.html', {'form': form, 'grup_id': grup_id})