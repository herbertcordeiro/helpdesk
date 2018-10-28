from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import RegistrationForm, EditForm, EditForm2
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from adminstrador.urls import inicial

@permission_required('polls.can_vote', login_url='inicial')
def register(request):
    form = RegistrationForm(request.POST, request.FILES, None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = RegistrationForm()
        args = {'form': form}   
        return render(request, 'newUser.html', args)

@permission_required('polls.can_vote', login_url='inicial')
def list_users(request):
    userList = User.objects.all()
    return render(request, 'users.html', {"userList": userList})

@permission_required('polls.can_vote', login_url='inicial')
def delete(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('users')

@permission_required('polls.can_vote', login_url='inicial')
def edit(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditForm(instance=user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

@login_required
def edit_perfil(request):
    if request.method == 'POST':
        form = EditForm2(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditForm2(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_perfil.html', args)