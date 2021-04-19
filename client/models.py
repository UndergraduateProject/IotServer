from django.db import models

# Create your models here.
class Client(models.Model):

    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    verify = models.IntegerField()
    enable = models.BooleanField(default=False)
