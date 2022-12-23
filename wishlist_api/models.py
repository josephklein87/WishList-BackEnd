from django.db import models

# Create your models here.
class Wishlist(models.Model):
   gift_picture = models.TextField(max_length=255)
   gift_name = models.CharField(max_length=50)
   gift_price = models.IntegerField()
   on_sale = models.BooleanField(default=False)
   link = models.TextField(max_length=255)
   tags = models.CharField(max_length=50)
   been_purchase = models.BooleanField(default=False)