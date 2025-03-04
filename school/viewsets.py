import json
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import School, Classroom
from .forms import SchoolForm, ClassroomForm

#  CRUD for School

@method_decorator(csrf_exempt, name='dispatch')
class SchoolViewSet(View):
    def get(self, request, *args, **kwargs):
        schools = School.objects.all()
        if not schools:
            return HttpResponse("No Schools Found")
        schools_data = [model_to_dict(school) for school in schools]
        return JsonResponse(schools_data, safe=False)

    def post(self, request, *args, **kwargs):
        request_body = request.body.decode("utf-8")
        print(request_body)  # Just to see incoming data during testing
        data = json.loads(request_body)
        form = SchoolForm(data)

        if form.is_valid():
            school = form.save()
            return JsonResponse(model_to_dict(school), status=201)
        return JsonResponse(form.errors, status=400)

    def put(self, request, *args, **kwargs):
        school_id = kwargs.get("pk")
        school = School.objects.get(id=school_id)
        request_body = request.body.decode("utf-8")
        data = json.loads(request_body)

        form = SchoolForm(data, instance=school)
        if form.is_valid():
            school = form.save()
            return JsonResponse(model_to_dict(school), status=200)
        return JsonResponse(form.errors, status=400)

    def delete(self, request, *args, **kwargs):
        school_id = kwargs.get("pk")
        school = School.objects.get(id=school_id)
        school.delete()
        return JsonResponse({"message": f"School {school_id} deleted"}, status=204)

#  CRUD for Classroom

@method_decorator(csrf_exempt, name='dispatch')
class ClassroomViewSet(View):
    def get(self, request, *args, **kwargs):
        classrooms = Classroom.objects.all()
        if not classrooms:
            return HttpResponse("No Classrooms Found")

        classrooms_data = [model_to_dict(classroom) for classroom in classrooms]
        return JsonResponse(classrooms_data, safe=False)

    def post(self, request, *args, **kwargs):
        request_body = request.body.decode("utf-8")
        print(request_body)
        data = json.loads(request_body)

        form = ClassroomForm(data)
        if form.is_valid():
            classroom = form.save()
            return JsonResponse(model_to_dict(classroom), status=201)
        return JsonResponse(form.errors, status=400)

    def put(self, request, *args, **kwargs):
        classroom_id = kwargs.get("pk")
        classroom = Classroom.objects.get(id=classroom_id)
        request_body = request.body.decode("utf-8")
        data = json.loads(request_body)

        form = ClassroomForm(data, instance=classroom)
        if form.is_valid():
            classroom = form.save()
            return JsonResponse(model_to_dict(classroom), status=200)
        return JsonResponse(form.errors, status=400)

    def delete(self, request, *args, **kwargs):
        classroom_id = kwargs.get("pk")
        classroom = Classroom.objects.get(id=classroom_id)
        classroom.delete()
        return JsonResponse({"message": f"Classroom {classroom_id} deleted"}, status=204)