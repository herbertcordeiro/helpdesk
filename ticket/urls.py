from django.urls import path
from .views import optionticket, searchticket, newticket, oxi, dashboard

urlpatterns = [
    path('newticket/', newticket, name='newticket'),
    path('optionticket/', optionticket, name='optionticket'),
    path('searchticket/', searchticket, name='searchticket'),
    path('oxi/', oxi, name='aff'),
    path('dashboard', dashboard, name='dashboard'),
]
