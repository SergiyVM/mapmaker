from django.contrib import admin
from .models import POI
from .models import POIType

admin.site.register(POI)
admin.site.register(POIType)