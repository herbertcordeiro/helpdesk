from django.urls import path
from .views import newUser, users, delete_users
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', users, name="users"),
    path('newUser/', newUser, name='newUser'),
    path('delete/<int:user_id>/', delete_users, name='user_delete'),
]