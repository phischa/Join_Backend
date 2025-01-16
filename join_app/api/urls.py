from django.urls import path, include
from .views import first_view, UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('first/', first_view),
]
