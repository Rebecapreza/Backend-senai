from django.db import models

class Autores(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField( max_length=30, null= True, blank=True)
    biografia = models.TextField(null=True, blank= True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"