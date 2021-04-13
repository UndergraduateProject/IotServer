from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.EmailField(max_length=None)
    enable = models.BooleanField()
