from django.shortcuts import render, get_object_or_404
from .forms import TicketForm

def newticket(request):
    form = TicketForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
    return render(request, 'newticket.html', {'form': form})

def optionticket(request):
    return render(request, 'optionticket.html', {})