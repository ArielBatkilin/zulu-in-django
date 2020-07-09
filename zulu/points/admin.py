
from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import point

@admin.register(point)
class pointsAdmin(OSMGeoAdmin):
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 12
    list_display = ('name', 'location')
