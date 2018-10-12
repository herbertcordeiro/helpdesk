from django.urls import path
from .views import newUser, users
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', users, name="users"),
    path('newUser/', newUser, name='newUser'),
]