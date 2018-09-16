from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('home', index, name='home'),
    path('tickets/', include('ticket.urls')),
    path('admin/', admin.site.urls)
]
