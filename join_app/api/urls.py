from django.urls import path, include
from .views import UserViewSet, TaskViewSet, ContactViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'task', TaskViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
