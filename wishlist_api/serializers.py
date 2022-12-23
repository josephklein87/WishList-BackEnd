from rest_framework import serializers 
from .models import Wishlist

class ContactSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Wishlist
        fields = ('id', 'gift_picture', 'gift_name', 'gift_price', 'on_sale', 'link', 'tags', 'been_purchased') 