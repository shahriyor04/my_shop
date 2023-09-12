from rest_framework.routers import DefaultRouter

from .views import ProductAPIViewSet, CategoryAPIViewSet
from django.urls import  path, include

router = DefaultRouter()
router.register('category', CategoryAPIViewSet, basename='category')
router.register('user', ProductAPIViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),

]

