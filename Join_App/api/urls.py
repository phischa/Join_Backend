from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, TaskViewSet, UserViewSet, hello_world

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')  

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', hello_world, name='hello_world'),
]
