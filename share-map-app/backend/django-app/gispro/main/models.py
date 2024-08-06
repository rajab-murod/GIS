from django.contrib.auth.models import User
from django.db import models


class ActionButton(models.Model):
    LINK_TYPE = (
        ('new_tab', 'New Tab'),
        ('same_tab', 'Same Tab'),
        ('modal', 'Modal'),
    )
    url = models.URLField(null=True, blank=True)
    btn_title = models.CharField(max_length=20, null=True, blank=True)
    open_link_in = models.CharField(choices=LINK_TYPE, default='new_tab', max_length=10)


class PositionView(models.Model):
    zoom_lvl = models.DecimalField(max_digits=5, decimal_places=2, default=12.00)
    effect_3d = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    lat = models.DecimalField(max_digits=15, decimal_places=12, default=0.00)
    long = models.DecimalField(max_digits=15, decimal_places=12, default=0.00)
    rotation = models.IntegerField(default=0)



class Marker(models.Model):
    MARKER_TYPE = (
        ('shape', 'Shape'),
        ('image', 'Image'),
    )
    marker_type = models.CharField(choices=MARKER_TYPE, default='shape', max_length=10)
    size = models.IntegerField(default=35, blank=True)
    image = models.FileField(upload_to='marker/', blank=True, null=True)
    color = models.CharField(max_length=15, default='#4D5E6AFF', blank=True)
    marker_text = models.CharField(max_length=255, null=True, blank=True)
    text_size = models.IntegerField(default=60, blank=True)


class Drawing(models.Model):
    MODE = (
        ('draw', 'Draw'),
        ('view', 'View'),
    )
    ZOOM = (
        ('always', 'Always'),
        ('zoom_range', 'Zoom Range'),
    )
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=15, default='#000000BF')
    mode = models.CharField(choices=MODE, default='view', max_length=5)
    zoom = models.CharField(choices=ZOOM, default='always', max_length=15)
    zoom_range = models.IntegerField(default=0)
    kml_file = models.FileField(upload_to='drawing/kml_file/', blank=True, null=True)



class Category(models.Model):
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='child', null=True, blank=True)
    name = models.CharField(max_length=255)
    marker = models.OneToOneField(Marker, on_delete=models.DO_NOTHING, blank=True, null=True)
    drawing = models.ManyToManyField(Drawing, blank=True, related_name='categories')



class Map(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Published'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    logo = models.FileField(upload_to='map/logo/', blank=True, null=True)
    action_btn = models.OneToOneField(ActionButton, on_delete=models.DO_NOTHING, blank=True, null=True)
    drawing = models.ManyToManyField(Drawing, blank=True, related_name='maps')
    status = models.CharField(choices=STATUS, default='draft', max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Published'),
    )
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    show_address = models.BooleanField(default=True)
    show_3d_building = models.BooleanField(default=False)
    desc = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True, related_name='locations')
    drawing = models.ManyToManyField(Drawing, blank=True, related_name='locations')
    action_btn = models.OneToOneField(ActionButton, on_delete=models.DO_NOTHING, blank=True, null=True)
    marker = models.OneToOneField(Marker, on_delete=models.DO_NOTHING, blank=True, null=True)
    position_view = models.OneToOneField(PositionView, on_delete=models.DO_NOTHING, blank=True, null=True)
    audio_file = models.FileField(upload_to='location/audio/', null=True, blank=True)
    status = models.CharField(choices=STATUS, default='draft', max_length=20)



class MediaFile(models.Model):
    MEDIA_TYPE = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('pdf', 'PDF'),
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='media_files')
    media_type = models.CharField(choices=MEDIA_TYPE, default='image', max_length=10)
    file = models.FileField(upload_to='media/', blank=True, null=True)



