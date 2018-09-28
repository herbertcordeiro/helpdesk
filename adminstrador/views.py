from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


@login_required
def inicial(request):
    filter = request.GET.get("filter", None)
    if(filter != None):
        tickets_list = Ticket.objects.filter(status=filter)
    else:
        tickets_list = Ticket.objects.order_by("status").all()
    paginator = Paginator(tickets_list, 5)
    page = request.GET.get('page')
    tickets = paginator.get_page(page) 
    return render(request, 'listartickets.html', {"tickets": tickets, 'filter': filter, 'page': page })


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
    return render(request, 'detailsticket.html', {'ticket': ticket})
