from django.urls import path
from .views import register, list_users, delete, perfil,edit
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', list_users, name="users"),
    path('register/', register, name='newUser'),
    path('perfil/', perfil, name='edit'),
    path('edit/<int:user_id>', edit, name='edit'),
]