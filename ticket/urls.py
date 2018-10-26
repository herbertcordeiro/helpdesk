from django.urls import path
from .views import register_ticket, view_ticket
from django.views.generic.base import TemplateView

urlpatterns = [
    path('register', register_ticket, name='newticket'),
    path('option', TemplateView.as_view(template_name='optionticket.html'), name="optionticket"),
    path('search', TemplateView.as_view(template_name='searchticket.html'), name='searchticket'),
    path('', view_ticket, name='id'),
]
