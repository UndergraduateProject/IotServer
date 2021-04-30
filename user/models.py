from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    owner = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    verify = models.IntegerField(default=999999)

    def __str__(self):
        return self.username