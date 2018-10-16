from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import UserForm
from django.contrib.auth.models import User

def newUser(request):
    form = UserForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect ('users')
    return render(request, 'newUser.html', {'form': form})
    
def users(request):
    userList = User.objects.values()
    return render(request, 'users.html', {"userList": userList})

def delete_users(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return HttpResponseRedirect('/users/')