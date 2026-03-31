from django.shortcuts import render,redirect, get_object_or_404
from .models import Tarefa
from datetime import date 


def listar_tarefas(request):
    if request.method=="GET":
        tarefas = Tarefa.objects.all()
        return render(request,"tarefa.html",{'tarefas':tarefas})

def criar_tarefa(request):
    if request.method=="GET":
        
        return render(request,'criar_tarefa.html')
    elif request.method=="POST":
        nome = request.POST.get('nome') 
        descricao = request.POST.get('descricao')
        prazo = request.POST.get('data')
        data = date.today()
        tarefa = Tarefa(nome=nome,descricao=descricao,prazo=prazo,data=data)
        tarefa.save()
        return redirect("listar_tarefas")

def concluir_tarefa(request,id):
    if request.method=="POST":
        tarefa = Tarefa.objects.get(id=id)
        tarefa.status = True
        tarefa.save()
        return redirect("listar_tarefas")

def excluir_tarefa(request,id):
    if request.method=="POST":
        tarefa = Tarefa.objects.get(id=id)
        tarefa.delete()
        return redirect("listar_tarefas")

def ver_tarefa(request,id):
    if request.method=="POST":
        tarefa = get_object_or_404(Tarefa, id=id)
        return render(request,"ver_tarefa.html",{"tarefa":tarefa})







