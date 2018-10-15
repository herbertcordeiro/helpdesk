from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.models import User

def newUser(request):
    form = UserForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        print('oxi')
    return render(request, 'newUser.html', {'form': form})
    
def users(request):
    userList = User.objects.values()
    return render(request, 'users.html', {"userList": userList})