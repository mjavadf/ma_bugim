from django.db import models

class Rule(models.Model):
    description = models.TextField()
    status = models.BooleanField(default=True)