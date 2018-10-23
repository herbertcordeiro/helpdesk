from django.urls import path
from .views import newUser, users, delete_users, edit
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', users, name="users"),
    path('newUser/', newUser, name='newUser'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:user_id>/', delete_users, name='user_delete'),
]