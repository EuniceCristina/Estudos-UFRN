from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa


def ver_user(request):
    
    if request.method=="GET":

        return render(request,'ver_user.html',{'nome':"Eunice"})
    elif request.method=="POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        pessoa = Pessoa(nome=nome,idade=idade)
        pessoa.save()
        pessoas = Pessoa.objects.all()
        pessoa1 = Pessoa.objects.filter(nome=nome)
        if pessoa1.exists():
            print(pessoa1)
        print(pessoas[0].idade)
        return render(request,'ver_user.html',{'nome':nome,'idade':idade})
def inserir_user(request):
    return HttpResponse('Inserindo produto')
        