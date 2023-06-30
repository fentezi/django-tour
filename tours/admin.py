from django.contrib import admin
from tours import models

# Register your models here.
admin.site.register(models.City)


@admin.register(models.Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['hotel_title', 'city']
