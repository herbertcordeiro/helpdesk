from django.forms import ModelForm
from ticket.models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']