from django.shortcuts import render
from django.views import View

from .models import Message

class SendePrivateMessage(View):
    def get(self, request, *args, **kwargs):
        
    