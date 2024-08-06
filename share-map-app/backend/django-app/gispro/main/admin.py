from django.contrib import admin
from .models import ActionButton, Map, Marker, Location,\
    PositionView, MediaFile, Category, Drawing


admin.site.register(ActionButton)
admin.site.register(Marker)
admin.site.register(Map)
admin.site.register(Location)
admin.site.register(PositionView)
admin.site.register(MediaFile)
admin.site.register(Category)
admin.site.register(Drawing)