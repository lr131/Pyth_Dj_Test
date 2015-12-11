from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.grups_list, name='grups_list'),
    url(r'^all_students/$', views.students_full_list, name='students_full_list'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^(?P<grup_id>[0-9]+)/$', views.students_list, name='students_list'),
    url(r'^create/$', views.grup_create, name='grup_create'),
    url(r'^edit/(?P<grup_id>[0-9]+)/$', views.grup_edit, name='grup_edit'),
    url(r'^delete/(?P<grup_id>[0-9]+)/$', views.grup_del, name='grup_del'),
    url(r'^delete/(?P<grup_id>[0-9]+)/confirm$', views.alarm_del, name='alarm_del'),
]