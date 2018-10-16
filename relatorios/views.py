import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket

@login_required
def relatorios(request):
    total=[]
    total_novo=0
    total_aberto=0
    total_fechado=0
    tickets = Ticket.objects.all()
    for i in tickets:
        if i.status=='1':
            total_novo=total_novo+1
        elif i.status=='2':
            total_aberto=total_aberto+1
        else:
            total_fechado=total_fechado+1
    total.append(total_novo)
    total.append(total_aberto)
    total.append(total_fechado)
    categoria = [obj.categoria.nome for obj in tickets]
    context = {
        'total': json.dumps(total),
        'categoria': json.dumps(categoria),
    }
    return render(request, 'relatorios.html', context)

