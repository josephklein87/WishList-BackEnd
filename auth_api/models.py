from django.db import models

# Create your models here.
class UserAccount(models.Model):
    email = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    username = models.CharField(max_length=20, default='admin')
    birthday = models.CharField(max_length=25, default='null')

class Follow(models.Model):
    user = models.ForeignKey(UserAccount, related_name='following', on_delete=models.CASCADE, default='null')
    following = models.ForeignKey(UserAccount, related_name='followers', on_delete=models.CASCADE)