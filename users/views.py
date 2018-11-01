from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import RegistrationForm, edit_photo_form, EditProfileForm, UserFormEdit
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from adminstrador.urls import inicial
from .models import UserProfile


@permission_required('polls.can_vote', login_url='inicial')
def register(request):
    form = RegistrationForm(request.POST, request.FILES, None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = RegistrationForm(instance=request.user)
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
        form = UserFormEdit(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserFormEdit(instance=user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


@login_required
def perfil(request):
        print(request.user)
        if request.method == 'POST':
                form = edit_photo_form(request.POST, request.FILES)
                form2 = EditProfileForm(request.POST, instance=request.user)
                if form.is_valid():
                        userProfile = UserProfile.objects.get(user=request.user.id)
                        if(form.cleaned_data['photo'] != None):
                                userProfile.image = form.cleaned_data['photo']
                        userProfile.save() 
                        form2.save()
                        return redirect('users')
        else:
                form = edit_photo_form()
                form2 = EditProfileForm(instance=request.user)
                return render(request, 'edit_perfil.html', {'form':form, 'form2':form2})