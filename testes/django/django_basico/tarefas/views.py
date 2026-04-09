from django.shortcuts import render, redirect
from datetime import datetime


# Create your views here.
from .models import Tarefa
from pessoas.models import Pessoa


def tarefa(request):
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()
        return render(request,'tarefa.html',{'tarefas':tarefas})
    
def tarefa_create(request):
    if request.method=='GET':
        return render(request,'tarefa_create.html')
    elif request.method=='POST':
        data = datetime.now()
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        prazo = request.POST.get('prazo')
        pessoa = Pessoa.objects.get(nome='Eunice')
        lista_prazo = datetime.strptime(prazo, "%Y-%m-%d")
        status = 'P'
        if lista_prazo <= data:
                    status = 'A'
        
        try:
            tarefa = Tarefa(nome=nome,descricao=descricao,prazo=prazo,status=status,pessoa=pessoa)
            tarefa.save()
            return redirect('tarefas:tarefa')
        except Exception as e:
            print(e)
            return redirect('tarefas:tarefa')
             
        

        


    