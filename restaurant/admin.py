from django.contrib import admin

from restaurant.models import Booking, Menu

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)