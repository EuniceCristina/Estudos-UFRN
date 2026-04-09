from django.urls import path
from . import views

app_name = 'tarefas'
urlpatterns = [
    path('tarefa/',views.tarefa,name='tarefa'),
    path('tarefa_create/' , views.tarefa_create, name='tarefa_create'),
    path('excluir_tarefa/<int:id>/' , views.excluir_tarefa, name='excluir_tarefa'),
    path('concluir_tarefa/<int:id>/' , views.concluir_tarefa, name='concluir_tarefa'),
]
