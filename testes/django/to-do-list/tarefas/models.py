from django.db import models

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(default='',max_length=100)
    descricao =models.CharField(max_length=255,default='')
    status = models.BooleanField(default=False)
    data = models.CharField(max_length=100,default='')
    prazo = models.CharField(max_length=100,default='')

    def __str__(self):
        
        return f"{self.nome} - {self.status}"


