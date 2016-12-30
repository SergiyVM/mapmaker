from django.contrib import admin
from .models import POI
from .models import POIType
from .models import Map

admin.site.register(Map)
admin.site.register(POI)
admin.site.register(POIType)