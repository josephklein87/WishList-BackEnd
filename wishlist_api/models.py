from django.db import models

# Create your models here.
class Wishlist(models.Model):
   gift_picture = models.TextField(max_length=255)
   gift_name = models.CharField(max_length=50)
   gift_price = models.DecimalField(decimal_places=2, max_digits=9)
   on_sale = models.BooleanField(default=False)
   link = models.TextField(max_length=1000)
   tags = models.CharField(max_length=50)
   been_purchase = models.BooleanField(default=False)
   posted_by = models.CharField(max_length=20, default='admin')