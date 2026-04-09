from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa
from tarefas import views


def user_login(request):
    if request.method == "GET":
        return render(request,'user_login.html')
    elif request.method == "POST":

        nome = request.POST.get("nome")
        senha = request.POST.get('senha')
        pessoa = Pessoa.objects.filter(nome=nome,senha=senha)
        if pessoa:
            return redirect('tarefas:tarefa')
        else:
            error = "Seu usuário ou senha estão incorretos. Tente novamente!"
            return render(request,'user_login.html', {'error':error})


    
def user_create(request):
    
    if request.method=="GET":

        return render(request,'user_create.html',{'nome':"Eunice"})
    elif request.method=="POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        senha = request.POST.get('senha')
        pessoa = Pessoa(nome=nome,idade=idade,senha=senha)
        pessoa.save()
        pessoas = Pessoa.objects.all()
        pessoa1 = Pessoa.objects.filter(nome=nome)
        if pessoa1.exists():
            print(pessoa1)
        print(pessoas[0].idade)
        return redirect('pessoas:user_login')
def inserir_user(request):
    return HttpResponse('Inserindo produto')
        