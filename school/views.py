from django.shortcuts import render, redirect, get_object_or_404
from .models import School, Classroom
from .forms import SchoolForm, ClassroomForm,DeleteSchoolForm

def home(request):
    return render(request, 'school/home.html', {
        'school_form': SchoolForm(),
        'classroom_form': ClassroomForm(),
        'delete_school_form': DeleteSchoolForm(), 
    })


def school_list(request):
    search = request.GET.get('search', '')
    schools = School.objects.all()

    if search:
        schools = schools.filter(name__icontains=search)

    return render(request, 'school/school_list.html', {
        'schools': schools,
        'search': search,
    })



def classroom_list(request):
    search = request.GET.get('search', '')
    classrooms = Classroom.objects.all()

    if search:
        classrooms = classrooms.filter(name__icontains=search)

    return render(request, 'school/classroom_list.html', {
        'classrooms': classrooms,
        'search': search,
    })

def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            school = form.save(commit=False)
            school.area = request.POST.get('area')  # use area from the form
            school.save()

            return render(request, 'school/home.html', {
                'school_form': SchoolForm(),
                'classroom_form': ClassroomForm(),
                'delete_school_form': DeleteSchoolForm(),
                'success_message': "School successfully added!"
            })
    return redirect('home')

def add_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.area = request.POST.get('area')  # use area from the form
            classroom.save()

            return render(request, 'school/home.html', {
                'school_form': SchoolForm(),
                'classroom_form': ClassroomForm(),
                'delete_school_form': DeleteSchoolForm(),
                'success_message': "Classroom successfully added!"
            })
    return redirect('home')


def delete_school(request):
    if request.method == 'POST':
        form = DeleteSchoolForm(request.POST)
        if form.is_valid():
            school = form.cleaned_data['school']
            school.delete()
            success_message = "School successfully deleted!"
            return render(request, 'school/home.html', {
                'school_form': SchoolForm(),
                'classroom_form': ClassroomForm(),
                'delete_school_form': DeleteSchoolForm(),  # Added this!
                'schools': School.objects.all(),
                'success_message': success_message
            })