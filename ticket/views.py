from django.shortcuts import render, get_object_or_404
from .forms import TicketForm
from .models import Ticket
from django.contrib import messages

def register_ticket(request):
    form = TicketForm(request.POST, request.FILES, None)
    if form.is_valid():
        ticket = form.save()
        context_dict = {'ticket': ticket}
        return render(request, 'viewticket.html', context = context_dict)
    return render(request, 'newticket.html', {'form': form})
    
def search_ticket(id):
    ticket = Ticket.objects.get(id=id)
    return ticket
      
def view_ticket(request):
    try:
        ticket = search_ticket(request.GET['id'])
        context_dict = {'ticket': ticket}
        return render(request, 'viewticket.html', context = context_dict)
    except:
        context_dict = {'ticket': None}
        messages.error(request, 'Ticket não existe')
        return render(request, 'searchticket.html',context = context_dict)


