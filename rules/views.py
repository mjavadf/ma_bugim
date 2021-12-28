from django.shortcuts import render
from .models import Rule

def welcome(request):
    rules = Rule.objects.filter(status=True)
    context = {'rules': rules}
    return render(request=request, 
                  template_name='rules/rules.html',
                  context=context)
