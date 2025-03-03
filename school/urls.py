from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, ClassroomViewSet

# Create a router for automatically generating routes
router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')

urlpatterns = [
    path('', include(router.urls)),  # Includes all generated URLs
]
