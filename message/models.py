from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    private = models.BooleanField(default=False)
    reciver = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='recived_messages')
    sender = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               related_name='sent_messages',
                               null=True,
                               blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
