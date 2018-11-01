from django.urls import path
from .views import register, list_users, delete, perfil, edit, edit_password
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', list_users, name="users"),
    path('register/', register, name='newUser'),
    path('perfil/', perfil, name='perfil'),
    path('edit/<int:user_id>', edit, name='edit'),
    path('editpassword/', edit_password, name='editpassword'),
]