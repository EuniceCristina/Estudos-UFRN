from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tarefas/', views.listar_tarefas,name='listar_tarefas'),
    path('criar_tarefa/',views.criar_tarefa,name='criar_tarefa'),
    path('concluir/<int:id>/',views.concluir_tarefa,name="concluir_tarefa"),
    path('excluir/<int:id>/',views.excluir_tarefa,name="excluir_tarefa"),
    path('ver_tarefa/<int:id>',views.ver_tarefa,name="ver_tarefa")
]
