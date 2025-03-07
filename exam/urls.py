from django.urls import path, include
from rest_framework.routers import DefaultRouter
from exam.views import ExamViewSet

router = DefaultRouter()
router.register(r"", ExamViewSet, basename="exam")

urlpatterns = [
    path("", include(router.urls)),
]
