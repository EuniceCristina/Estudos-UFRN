from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.get_works,name='get_works_all'),
    path('tarefa/<str:titulo>/',views.get_by_title,name='get_by_title'),
    path('data/',views.work_manager,name='work_manager')
]

