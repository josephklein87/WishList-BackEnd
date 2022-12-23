from django.shortcuts import render# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .serializers import ContactSerializer
from .models import Wishlist

class ContactList(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all().order_by('id') 
    serializer_class = ContactSerializer 

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all().order_by('id')
    serializer_class = ContactSerializer
