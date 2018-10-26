from django.urls import path, re_path
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm,password_reset_complete
    
    
urlpatterns = [ 
    path('esqueceu-senha/', password_reset, name='esqueceu-senha'),
    path('login/', password_reset_done, name='password_reset_done'),
    re_path('esqueceu-senha/confirmacao/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', password_reset_confirm, name='password_reset_confirm'),
    path('login/', password_reset_complete, name='password_reset_complete'),
    
]