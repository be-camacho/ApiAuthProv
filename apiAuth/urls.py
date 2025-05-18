from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet as UV

router = DefaultRouter()
router.register('users',UV,'user')

urlpatterns = [
    path('api/', include(router.urls)),
]