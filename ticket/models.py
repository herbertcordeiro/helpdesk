from django.db import models
from datetime import timedelta, datetime

class Categoria(models.Model):
    nome=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Ticket(models.Model):
    STATUS = (
        ('1', 'NOVO'),
        ('2', 'ABERTO'),
        ('3', 'FECHADO')
    )
    status = models.CharField(max_length=1, null=True, choices=STATUS, default='1')
    data_criacao = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    data_entrega = models.DateTimeField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    nome_completo = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    anexo = models.FileField(upload_to='post_image', blank=True)
    descricao = models.TextField()

