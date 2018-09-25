from django.db import models

class Categoria(models.Model):
    nome=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Ticket(models.Model):
    STATUS = (
        ('1', 'novo'),
        ('2', 'resolvido'),
        ('3', 'em progresso')
    )
    STATUS = models.CharField(max_length=1, null=True, choices=STATUS, default='1')
    data_criacao=models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    nome_completo = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    anexo = models.FileField(upload_to='post_image', blank=True)
    descricao = models.TextField()

