from django.contrib import admin
from .models import Equipment, Client, Rental


admin.site.register(Equipment)
admin.site.register(Client)
admin.site.register(Rental)