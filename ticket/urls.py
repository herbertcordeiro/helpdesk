from django.urls import path
from .views import newticket 
from .views import optionticket

urlpatterns = [
    path('newticket/', newticket),
    path('optionticket/', optionticket, name='oxi'),
]
