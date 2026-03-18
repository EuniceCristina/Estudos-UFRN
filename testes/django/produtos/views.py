from django.shortcuts import render
from django.http import HttpResponse


def ver_produto(request):
    
    if request.method=="GET":

        return render(request,'ver_produto.html',{'nome':"Eunice"})
    elif request.method=="POST":
        numero = request.POST.get('numero')
        valor = request.POST.get('valor')
        return render(request,'ver_produto.html',{'numero':numero,'nome':"Eunice"})
def inserir_produto(request):
    return HttpResponse('Inserindo produto')
        