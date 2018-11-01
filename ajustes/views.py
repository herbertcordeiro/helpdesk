from django.shortcuts import render
from .forms import CategoriaForm
from ticket.models import Categoria

def register_categoria(request):
    form = CategoriaForm(request.POST, request.FILES, None)
    if form.is_valid():
        categoria = form.save()
        context_dict = {'categoria': categoria}
        return render(request, 'ajustes.html', context = context_dict)
    return render(request, 'ajustes.html', {'form': form})
