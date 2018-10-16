from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from adminstrador.urls import inicial

@permission_required('polls.can_vote', login_url='inicial')
def newUser(request):
    form = UserForm(request.POST, request.FILES, None)
    if form.is_valid():
        nome = form.cleaned_data['first_name']
        sobrenome = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        senha = form.cleaned_data['password']
        new_user = User.objects.create_user(first_name=nome, last_name=sobrenome,email=email,username=username,password=senha)
        new_user.save()
        return redirect ('users')
    return render(request, 'newUser.html', {'form': form})

@permission_required('polls.can_vote', login_url='inicial')
def users(request):
    userList = User.objects.values()
    return render(request, 'users.html', {"userList": userList})

@permission_required('polls.can_vote', login_url='inicial')
def delete_users(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return HttpResponseRedirect('/users/')