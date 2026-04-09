from django.urls import path
from . import views

app_name = 'tarefas'
urlpatterns = [
    path('tarefa/',views.tarefa,name='tarefa'),
    path('tarefa_create/' , views.tarefa_create, name='tarefa_create'),
]
