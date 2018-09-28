from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


@login_required
def inicial(request):
    tickets_list = Ticket.objects.all()
    paginator = Paginator(tickets_list, 5)
    page = request.GET.get('page')
    tickets = paginator.get_page(page)
    return render(request, 'listartickets.html', {"tickets": tickets})


@login_required
def pesquisa_id_nome(request):
    filter = request.GET.get("id", None)
    if(filter != None):
        tickets2 = Ticket.objects.filter(id=filter)
    else:
        tickets2 = Ticket.objects.all()
    return render(request, 'listartickets.html', {"tickets": tickets2})

