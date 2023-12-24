from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Project, Tasks
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request, user):
    return HttpResponse("Hello, %s" % user)


def about(request, id):
    return HttpResponse("Me: %s" % id)


def projects(request):
    projects_list = list(Project.objects.values())
    return JsonResponse(projects_list, safe=False)


def tasks(request, title):
    task = get_object_or_404(Tasks, title=title)
    return HttpResponse("Tasks: %s" % task.title)
