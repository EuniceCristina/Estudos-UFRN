from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField()
    idade = models.IntegerField()
    
    def __str__(self)->str:
        return self.nome