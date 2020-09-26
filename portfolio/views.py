from django.shortcuts import render
from .models import Project


# render will always return from insider templates folder
# You have to keep your .html file in a separate folder under 'templates' folder
# { 'projects': projects}) this means passing project perameter (2nd project) and reference first project perameter for the desired HTML file

def home(request):
    projects = Project.objects.all()
    count = Project.objects.count() # count is being used to determine weather it should display "My Projects or not"
    return render(request, 'portfolio/menu.html', {'projects': projects, 'count': count})


def projects(request):
    return render(request, 'portfolio/projects.html')