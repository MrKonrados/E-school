from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.student_create_or_edit, name='student_create_or_edit')
]