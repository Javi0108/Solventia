from django.db import models


class Queue(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    color = models.CharField(max_length=7)
