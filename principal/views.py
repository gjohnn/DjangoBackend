from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Project, Tasks
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    title = "Welcome to Project papu"
    return render(request, 'index.html', {
        "title": title,
        "creator": "Juan"
    })


def home(request, user):
    return render(request, )


def about(request, id):
    return HttpResponse("Me: %s" % id)


def projects(request):
    # projects_list = list(Project.objects.values())
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {
        "all_projects": all_projects
    })


def tasks(request):
    all_tasks = Tasks.objects.all()
    #return JsonResponse(all_tasks)
    return render(request, 'tasks/tasks.html', {"tasks": all_tasks})
