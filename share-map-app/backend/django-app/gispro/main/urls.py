from rest_framework.routers import DefaultRouter
from .views import MapViewSet, DrawingViewSet,\
    CategoryViewSet, MarkerViewSet, LocationViewSet,\
    ActionButtonViewSet, PositionViewSet

router = DefaultRouter()
router.register(r'map', MapViewSet, basename='map')
router.register(r'drawing', DrawingViewSet, basename='drawing')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'actionbtn', ActionButtonViewSet, basename='actionbtn')
router.register(r'position', PositionViewSet, basename='position')
router.register(r'marker', MarkerViewSet, basename='marker')
router.register(r'location', LocationViewSet, basename='location')
# router.register(r'login', LoginViewSet, basename='login')
# router.register(r'logout', LogOutViewSet, basename='logout')

urlpatterns = router.urls