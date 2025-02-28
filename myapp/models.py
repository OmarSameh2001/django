from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Name")
    capacity = models.PositiveIntegerField(verbose_name="Capacity")
    teacher = models.CharField(max_length=100, verbose_name="Teacher")

class classarea(models.Model):
    length=models.IntegerField(verbose_name="classlength")
    width=models.IntegerField(verbose_name="classlength")