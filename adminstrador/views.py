from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket

@login_required
def inicial(request):
    tickets = Ticket.objects.all()
    return render(request, 'listartickets.html', {"tickets": tickets})