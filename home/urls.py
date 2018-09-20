from django.contrib import admin
from django.urls import path
from .views import home
from .views import myLogout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', myLogout, name='logout'),

]
