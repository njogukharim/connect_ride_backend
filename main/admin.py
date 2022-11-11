from django.contrib import admin

from main import models

admin.site.register(models.Category)
admin.site.register(models.Order)
admin.site.register(models.User)
admin.site.register(models.Vehicle)
admin.site.register(models.VehicleImages)
