from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket

@login_required
def inicial(request):
    filter = request.GET.get("filter", None)
    if(filter != None):
        tickets = Ticket.objects.filter(status=filter)
    else:
        tickets = Ticket.objects.all()
    return render(request, 'listartickets.html', {"tickets": tickets})


@login_required
def pesquisa_id_nome(request):
    filter = request.GET.get("id", None)
    
    if(filter != None):
        tickets2 = Ticket.objects.filter(id=filter)
    else:
        tickets2 = Ticket.objects.all()
        
    return render(request, 'listartickets.html', {"tickets": tickets2})