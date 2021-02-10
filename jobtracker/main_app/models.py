from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
  company = models.CharField(max_length=80)
  title = models.CharField(max_length=80)
  location = models.CharField(max_length=80)
  active = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title + ' Application at ' + self.company

  def get_absolute_url(self):
    return reverse('detail', kwargs={'app_id': self.id})
  
  class Meta:
    ordering = ['id']

class Interview(models.Model):
  date = models.DateField()
  interviewer = models.CharField(max_length=50)
  notes = models.TextField(max_length=250)
  application = models.ForeignKey(Application, on_delete=models.CASCADE)

  class Meta:
    ordering = ['-date']