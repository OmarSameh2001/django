from django import forms
from .models import School, Classroom

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'
