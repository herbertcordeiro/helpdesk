from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password',
            'last_name',
            'first_name'
        ]
        