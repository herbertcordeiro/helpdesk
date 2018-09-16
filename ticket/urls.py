from django.urls import path
from .views import optionticket, searchticket, newticket, oxi

urlpatterns = [
    path('newticket/', newticket, name='newticket'),
    path('optionticket/', optionticket, name='optionticket'),
    path('searchticket/', searchticket, name='searchticket'),
    path('oxi/', oxi, name='aff'),
]
