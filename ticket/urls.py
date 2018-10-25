from django.urls import path
from .views import newticket, mostrar_ticket
from django.views.generic.base import TemplateView

urlpatterns = [
    path('/register', newticket, name='newticket'),
    path('/option', TemplateView.as_view(template_name='optionticket.html'), name="optionticket"),
    path('/search', TemplateView.as_view(template_name='searchticket.html'), name='searchticket'),
    path('', mostrar_ticket, name='id'),
]
