from django.db import models

# Create your models here.


class Client(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    verify = models.IntegerField(default=999999)
    enable = models.BooleanField(default=False)
