from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import TicketForm
from django.shortcuts import redirect

@login_required
def inicial(request):
    if(request.user.is_superuser):
        tickets_list = Ticket.objects.all()
    else:
        tickets_list = Ticket.objects.filter(user=request.user)     
    paginator = Paginator(tickets_list, 5)
    page = request.GET.get('page')
    tickets = paginator.get_page(page) 
    return render(request, 'listartickets.html', {"tickets": tickets, 'filter': filter, 'page': page })


@login_required
def pesquisa_id(request):
    filter = request.GET.get("id", None)
    if(filter != None):
        tickets2 = Ticket.objects.filter(user=request.user).filter(id=filter)  
    else:
        tickets2 = Ticket.objects.all()
    return render(request, 'listartickets.html', {"tickets": tickets2})

@login_required
def details(request, id):
    ticket = Ticket.objects.get(id = id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        form.save()
        return redirect('inicial')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'detailsticket.html', {'ticket': ticket, 'form': form})