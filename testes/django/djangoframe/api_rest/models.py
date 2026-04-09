from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100, default='')
    descricao = models.CharField(max_length=255,default='')
    prazo = models.DateField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    situação = models.CharField(max_length=100,default="")
    
    def __str__(self):
        return f'Titulo : {self.titulo} | Descricao : {self.descricao}'


    
