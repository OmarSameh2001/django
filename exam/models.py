from django.db import models
from django.conf import settings
from course.models import Course
from accounts.models import User

class Exam(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="exam_files/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.course.name}"
