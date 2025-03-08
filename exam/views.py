from rest_framework import viewsets
from .models import Exam
# from .serializers import ExamSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ExamViewSet(viewsets.ModelViewSet):
    # serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:  # Superusers can see all exams
            return Exam.objects.all()
        return Exam.objects.filter(user=user)  # Regular users can only see their exams
