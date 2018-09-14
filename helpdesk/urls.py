from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('', index),
    path('tickets/', include('ticket.urls')),
    path('admin/', admin.site.urls)
]
