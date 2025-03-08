from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ["title", "course", "date", "file", "user"]
