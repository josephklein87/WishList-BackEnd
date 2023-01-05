from django.contrib import admin

# Register your models here.
from .models import UserAccount
admin.site.register(UserAccount)

from .models import Follow
admin.site.register(Follow)