from django.urls import path
from . import views


urlpatterns = [
    path('api/gifts', views.ContactList.as_view(), name='contact_list'), 
    path('api/gifts/<int:pk>', views.ContactDetail.as_view(), name='contact_detail'), 
]