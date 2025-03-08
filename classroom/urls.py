from django.urls import path, include
from classroom.viewsets import ClassRoomView, ClassRoomViewSet
from classroom.views import home, csrf_obtain
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"classroom", ClassRoomViewSet, basename="classroom")

urlpatterns = [
    path("home/<str:david>/", home, name="home"),
    path("csrf/", csrf_obtain, name="csrf"),
    # path("classroom/<str:class_name>/", retreive_classroom, name="classroom"),
    path("classroom-view/", ClassRoomView.as_view(), name="classroom"),
    path("classroom-view/<int:pk>/", ClassRoomView.as_view(), name="classroom"),
    path("", include(router.urls)),
]