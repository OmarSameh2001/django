from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, name):
    return HttpResponse(f"Hello {name}")
    #return render(request, 'home.html')

# def retriveclassroom(request, class_name):
#     context = { 
#         "title":class_name,
#         "description":"this is a class this just a filler to check the funcationality of the if function inside index.html"
#     }
#     return render(request,"index.html", context)  