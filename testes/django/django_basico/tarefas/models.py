from django.db import models
from pessoas.models import Pessoa

# Create your models here.
class Tarefa(models.Model):

    STATUS_CHOICES = [
        ('P','Pendente'),
        ('A','Andamento'),
        ('C','Concluída')
    ]
    nome = models.CharField(default='',max_length=100)
    descricao = models.CharField(default='',max_length=255)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    prazo = models.CharField(default='',max_length=100)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='tarefas')