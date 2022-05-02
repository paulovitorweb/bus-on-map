from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Route

admin.site.register(Route, LeafletGeoAdmin)