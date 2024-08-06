from rest_framework import viewsets
from .models import Map, Drawing, Category, Location, Marker,\
    ActionButton, PositionView
from .serializers import MapSerializer,\
    DrawingSerializer, CategorySerializer, LocationSerializer,\
    ActionBtnSerializer, PositionViewSerializer, MarkerSerializer


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = PositionView.objects.all()
    serializer_class = PositionViewSerializer


class ActionButtonViewSet(viewsets.ModelViewSet):
    queryset = ActionButton.objects.all()
    serializer_class = ActionBtnSerializer


class DrawingViewSet(viewsets.ModelViewSet):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
