import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from users.views import listar_usuarios
from users.forms import User
from adminstrador.views import listartickets
from django.contrib.auth.models import User

@login_required
def relatorios(request):
    nomes=[]
    total=[]
    tick=[]
    temp=[]
    total_novo=0
    total_aberto=0
    total_fechado=0
    tickets = listartickets(request)
    for i in tickets:
        if i.status=='1':
            total_novo=total_novo+1
        elif i.status=='2':
            total_aberto=total_aberto+1
        else:
            total_fechado=total_fechado+1
    usuarios=listar_usuarios(request)
    for i in usuarios:
        nomes.append(i.username)   
    total.append(total_novo)
    total.append(total_aberto)
    total.append(total_fechado)
    context = {
        'total': json.dumps(total),
        'nomes': json.dumps(nomes),
        'tick': json.dumps(tick),
    }
    return render(request, 'relatorios.html', context, {"total":total})


def separar_tickets(request):
    tickets_abertos=[]
    tickets_fechados=[]
    tickets_novo=[]
    tickets = listartickets(request)
    usuarios=listar_usuarios(request)
    for i in tickets:
        if i.status=='1':
            tickets_novo.append(i)
        elif i.status=='2':
            tickets_abertos.append(i)
        else:
            tickets_fechados.append(i)
    
    

