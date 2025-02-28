from django.urls import path

from . import views, retriveclassroom

urlpatterns = [
    path("<str:name>/", views.home, name="home"),
    path("classroom/<str:class_name>/", retriveclassroom, name="classroom_detail")
]
