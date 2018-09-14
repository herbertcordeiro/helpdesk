from django.contrib import admin
from django.urls import path, include
from .views import index
from ticket import urls as tickets_urls


urlpatterns = [
    path('', index),
    path('tickets/', include(tickets_urls)),
    path('admin/', admin.site.urls)
]
