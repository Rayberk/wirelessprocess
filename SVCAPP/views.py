from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

 

def homepage(req):
    return render(req, 'SVCAPP/svc.html')
def process(req):
    return render(req, 'SVCAPP/output.html')
