from django.db import models

# Create your models here.
class UserAccount(models.Model):
    email = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    username = models.CharField(max_length=20, default='admin')
    friends = models.ManyToManyField('self', null=True, blank=True)