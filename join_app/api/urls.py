from django.urls import path, include
from .views import UserViewSet, TaskViewSet, ContactViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
