from django.shortcuts import render, get_object_or_404
from .forms import TicketForm
from .models import Ticket

def newticket(request):
    form = TicketForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
    return render(request, 'newticket.html', {'form': form})

def optionticket(request):
    return render(request, 'optionticket.html')

def searchticket(request):
    return render(request, 'searchticket.html')

def oxi(request):
    ticket = Ticket.objects.get(id=request.GET['aff'])
    context_dict = {'ticket': ticket}
    return render(request, 'mostrarticket.html', context= context_dict)