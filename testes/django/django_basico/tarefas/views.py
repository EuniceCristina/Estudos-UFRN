from django.shortcuts import render, redirect
from datetime import datetime


# Create your views here.
from .models import Tarefa
from pessoas.models import Pessoa


def tarefa(request):
    if request.method == 'GET':
        tarefa_A = Tarefa.objects.filter(status='A')
        tarefa_P = Tarefa.objects.filter(status='P')
        tarefa_C = Tarefa.objects.filter(status='C')
        return render(request,'tarefa.html',{'tarefa_A':tarefa_A,'tarefa_P':tarefa_P,'tarefa_C':tarefa_C})
    
def tarefa_create(request):
    if request.method=='GET':
        return render(request,'tarefa_create.html')
    elif request.method=='POST':
        data = datetime.now().date()
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        prazo = request.POST.get('prazo')
        pessoa = Pessoa.objects.get(nome='Eunice')
        lista_prazo = datetime.strptime(prazo, "%Y-%m-%d").date()
        print(lista_prazo.year)
        print(data.day)
        status = 'P'
        if lista_prazo >= data:
            
            status = 'A'
        
        try:
            tarefa = Tarefa(nome=nome,descricao=descricao,prazo=prazo,status=status,pessoa=pessoa)
            tarefa.save()
            return redirect('tarefas:tarefa')
        except Exception as e:
            print(e)
            return redirect('tarefas:tarefa')
        
def excluir_tarefa(request,id):
    if request.method=='POST':
        tarefa = Tarefa.objects.filter(id=id).first()
        if tarefa:
            tarefa.delete()
        return redirect('tarefas:tarefa')
    
def concluir_tarefa(request, id):
    if request.method=='POST':
        tarefa = Tarefa.objects.filter(id=id).first()
        tarefa.status = 'C'
        tarefa.save()
        return redirect('tarefas:tarefa')
        
        
    
             
        

        


    