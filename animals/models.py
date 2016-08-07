from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Specie(models.Model):
  scientific_name = models.CharField(max_length=255)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Animal(models.Model):
  user = models.ForeignKey(User)
  specie = models.ForeignKey(Specie, on_delete=models.SET_NULL, blank=True, null=True)
  name = models.CharField(max_length=255)
  physical_description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)