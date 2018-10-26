from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1',
            'password2',
            'last_name',
            'first_name',
            'is_superuser'
        ]
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.is_superuser = self.cleaned_data['is_superuser']
        if commit:
            user.save()

        return user

class EditForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'last_name',
            'first_name',
            'password',
            'is_superuser'
        )