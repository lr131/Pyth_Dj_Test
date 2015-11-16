from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.grups_list, name='grups_list'),
    url(r'^(?P<grup_id>[0-9]+)/$', views.students_list, name='students_list'),
    url(r'^create/$', views.grup_create, name='grup_create'),
    url(r'^edit(?P<grup_id>[0-9]+)/$', views.grup_edit, name='grup_edit'),
]
