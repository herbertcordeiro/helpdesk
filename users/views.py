from django.shortcuts import render
from .forms import UserForm

def newUser(request):
    form = UserForm(request.POST, request.FILES, None)
    if form.is_valid():
        user = form.save()
    return render(request, 'newUser.html', {'form': form})
    
