from django.contrib import admin
from django.urls import path
from .views import myLogout
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('logout/', myLogout, name='logout'),

]
