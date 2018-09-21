from django.shortcuts import render, get_object_or_404
from .forms import TicketForm
from .models import Ticket
from django.contrib.auth.decorators import login_required

def newticket(request):
    form = TicketForm(request.POST, request.FILES, None)
    if form.is_valid():
        ticket = form.save()
        context_dict = {'ticket': ticket}
        return render(request, 'mostrarticket.html', context = context_dict)
    return render(request, 'newticket.html', {'form': form})

def optionticket(request):
    return render(request, 'optionticket.html')

def searchticket(request):
    return render(request, 'searchticket.html')

def pesquisa_ticket(id):
    ticket = Ticket.objects.get(id=id)
    return ticket

def oxi(request):
    ticket = pesquisa_ticket(request.GET['aff'])
    context_dict = {'ticket': ticket}
    return render(request, 'mostrarticket.html', context = context_dict)

def dashboard(request):
    return render(request, 'basedashboard.html')