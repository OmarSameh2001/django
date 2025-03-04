from django.urls import path
from .viewsets import SchoolViewSet, ClassroomViewSet
from .views import school_list, classroom_list, home, add_school, add_classroom, delete_school

urlpatterns = [
    # Web Page Views (HTML Templates)
    path('', home, name='home'),
    path('school-list/', school_list, name='school-list'),
    path('classroom-list/', classroom_list, name='classroom-list'),
    path('add-school/', add_school, name='add-school'),
    path('add-classroom/', add_classroom, name='add-classroom'),
    path('delete-school/', delete_school, name='delete-school'),

    # API Endpoints (JSON)
    path('api/schools/', SchoolViewSet.as_view(), name='api-school-list'),
    path('api/schools/<int:pk>/', SchoolViewSet.as_view(), name='api-school-detail'),
    path('api/classrooms/', ClassroomViewSet.as_view(), name='api-classroom-list'),
    path('api/classrooms/<int:pk>/', ClassroomViewSet.as_view(), name='api-classroom-detail'),
]