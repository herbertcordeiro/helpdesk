from django.shortcuts import redirect
from django.contrib.auth import logout

def myLogout(request):
    logout(request)
    return redirect('home')