from django.urls import path
from .views import optionticket, searchticket, newticket, mostrar_ticket

urlpatterns = [
    path('newticket/', newticket, name='newticket'),
    path('optionticket/', optionticket, name='optionticket'),
    path('searchticket/', searchticket, name='searchticket'),
    path('mostrar_ticket/', mostrar_ticket, name='id'),
]
