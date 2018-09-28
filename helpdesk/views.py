from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request, exception, template_name='page404.html'):
    return render(request, 'page404.html')

def handler500(request):
    return render(request, 'page500.html', status=500)