from django.urls import path

from . import views

urlpatterns = [
    path("<str:name>/", views.home, name="home"),
    # path("classroom/<str:class_name>/", retriveclassroom, name="classroom_detail")
]
