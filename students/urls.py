from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^edit/(?P<grup_id>[0-9]+)/student/(?P<st_id>[0-9]+)/$', views.student_edit, name='student_edit'),
    url(r'^new/(?P<grup_id>[0-9]+)/$', views.student_create, name='student_create'),
    url(r'^delete/(?P<grup_id>[0-9]+)/student/(?P<st_id>[0-9]+)/$', views.student_del, name='student_del'),
]
