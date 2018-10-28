from django.urls import path
from .views import register, list_users, delete, edit, edit_perfil
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', list_users, name="users"),
    path('register/', register, name='newUser'),
    path('edit/<int:user_id>', edit, name='edit'),
    path('delete/<int:user_id>', delete, name='delete'),
    path('edit_perfil/', edit_perfil, name='edit_perfil'),
]