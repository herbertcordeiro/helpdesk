from django.urls import path
from .views import newUser

urlpatterns = [
     path('newUser/', newUser, name='newUser'),
]