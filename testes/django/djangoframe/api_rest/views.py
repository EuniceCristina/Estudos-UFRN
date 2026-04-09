from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Tarefa
from .serializers import TarefaSerializer
import json

@api_view(['GET'])
def get_works(request):
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas,many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_title(request, titulo):
    try:
        tarefa = Tarefa.objects.get(titulo=titulo)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)
    
@api_view(['GET','POST','PUT','DELETE'])
def work_manager(request):
    if request.method=='GET':
            try:
                titulo = request.GET["titulo"]


                try:
                    tarefa = Tarefa.objects.get(titulo=titulo)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = TarefaSerializer(tarefa)
                return Response(serializer.data)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
    
    if request.method=='POST':
        new_work = request.data

        serializer = TarefaSerializer(data=new_work)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        titulo = request.data['titulo']
        updated_user = Tarefa.objects.get(titulo=titulo)

        print(request.data)

        serializer = TarefaSerializer(updated_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
   





