from django.db import models


class Issues(models.Model):
    decription = models.TextField(blank=True)
    urgent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    closed_at = models.DateTimeField()
