from django.urls import path
from .views import newticket

urlpatterns = [
    path('newticket/', newticket),
]
