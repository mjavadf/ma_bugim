from django import forms
from .models import Message

class PrivateMessageForm(forms.Form):
    model = Message
    fields = ['reciver', 'text']