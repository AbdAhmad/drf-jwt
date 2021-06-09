from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    link = models.CharField(max_length=200, blank=True, default='')
    creator = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    created_on = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.title}"