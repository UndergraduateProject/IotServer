from django.db import models

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class LED(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name =  models.CharField(max_length=100, blank=True, default='')
    gpio_num = models.IntegerField(default=0)
    color = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')
    onoff = models.BooleanField(default=False)

    users = models.ForeignKey('auth.User',related_name='LEDs',on_delete=models.CASCADE)
    authenti_testing = models.CharField(max_length=100, blank=True, default='No authentication')

    class Meta:
        ordering = ['color']
    
