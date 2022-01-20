from django.contrib import admin
from .models import Profile ,Order,Comments,rate
# Register your models here.
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Comments)
admin.site.register(rate)