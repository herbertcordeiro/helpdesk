from django.urls import path
from .views import newticket, mostrar_ticket
from django.views.generic.base import TemplateView

urlpatterns = [
    path('newticket/', newticket, name='newticket'),
    path('optionticket/', TemplateView.as_view(template_name='optionticket.html'), name="optionticket"),
    path('searchticket/', TemplateView.as_view(template_name='searchticket.html'), name='searchticket'),
    path('mostrar_ticket/', mostrar_ticket, name='id'),
]
