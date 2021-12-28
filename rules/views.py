from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request=request, template_name='rules/rules.html')
