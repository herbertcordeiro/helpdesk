from django.shortcuts import render, get_object_or_404
from .forms import TicketForm
from .models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def newticket(request):
    form = TicketForm(request.POST, request.FILES, None)
    if form.is_valid():
        ticket = form.save()
        context_dict = {'ticket': ticket}
        return render(request, 'mostrarticket.html', context = context_dict)
    return render(request, 'newticket.html', {'form': form})
    
def pesquisa_ticket(id):
    ticket = Ticket.objects.get(id=id)
    return ticket
      
def mostrar_ticket(request):
    try:
        ticket = pesquisa_ticket(request.GET['id'])
        context_dict = {'ticket': ticket}
        return render(request, 'mostrarticket.html', context = context_dict)
    except:
        context_dict = {'ticket': None}
        messages.error(request, 'Ticket não existe')
        return render(request, 'searchticket.html',context = context_dict)


