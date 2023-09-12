from rest_framework.routers import DefaultRouter

from .views import ClientApiModelViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('Client', ClientApiModelViewSet, basename='Client')

urlpatterns = [
    path('', include(router.urls)),

]
