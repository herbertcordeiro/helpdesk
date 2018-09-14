from django.shortcuts import render
from .forms import TicketForm

def newticket(request):
    form = TicketForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
    return render(request, 'newticket.html', {'form': form})