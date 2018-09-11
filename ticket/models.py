from django.db import models

class Ticket(models.Model):
    banheiro = '1'
    sala = '2'
    labs = '3' 
    
    CATEGORIAS = (
        (banheiro, 'BANHEIRO'),
        (sala, 'SALA'),
        (labs, 'LABS'),
    )
    
    nome_completo = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    categoria = models.CharField(max_length=1, choices=CATEGORIAS)
    anexo = models.FileField(upload_to='post_image', blank=True)
    descricao = models.TextField()

