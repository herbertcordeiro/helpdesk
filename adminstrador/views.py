from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from ticket.forms import TicketForm

@login_required
def inicial(request):
    tickets_list = listaDeTickts(request)
    paginator = Paginator(tickets_list, 5)
    page = request.GET.get('page')
    tickets = paginator.get_page(page) 
    return render(request, 'listartickets.html', {"tickets": tickets, 'filter': filter, 'page': page })

@login_required
def listaDeTickts(request):
    tickets = Ticket.objects.all()
    tickets2 = []
    if(request.user.is_superuser):
        return tickets
    else:
        for ticket in tickets:
            if(ticket.user == request.user):
                tickets2.append(ticket)
        return tickets2

@login_required
def pesquisa_id(request):
    filter = request.GET.get("id", None)
    if(filter != None):
        tickets2 = Ticket.objects.filter(id=filter)
    else:
        tickets2 = Ticket.objects.all()
    return render(request, 'listartickets.html', {"tickets": tickets2})

@login_required
def details(request, id):
    ticket = Ticket.objects.get(id = id)
    form = TicketForm(instance=ticket)
    return render(request, 'detailsticket.html', {'ticket': ticket, 'form': form})
