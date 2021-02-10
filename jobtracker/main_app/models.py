from django.db import models

# Create your models here.
class Applications(models.Model):
  company = models.CharField(max_length=80)
  title = models.CharField(max_length=80)
  location = models.CharField(max_length=80)
  active = models.BooleanField(default=True)
  