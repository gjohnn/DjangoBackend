from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Project, Tasks
from django.shortcuts import get_object_or_404
from .forms import CreateTask, CreateProject


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
    return render(request, 'projects/projects.html', {
        "all_projects": all_projects
    })


def projectdetail(request, id):
    print(id)
    found_project = get_object_or_404(Project, id=id)
    tasks = Tasks.objects.filter(project_id=id)
    print(found_project)
    return render(request, "projects/project_detail.html", {
        "found_project": found_project,
        "tasks": tasks,
        "tab_title": "ProjectosApp - Projects"
    })


def createproject(request):
    if request.method == "GET":
        return render(request, 'projects/createProjects.html', {
            "form": CreateProject
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')


def tasks(request):
    all_tasks = Tasks.objects.all()  # return JsonResponse(all_tasks)
    return render(request, 'tasks/tasks.html', {"tasks": all_tasks})


def createtask(request):
    if request.method == 'GET':
        return render(request, 'tasks/createTask.html', {
            "form": CreateTask()
        })
    elif request.method == "POST":
        Tasks.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect("tasks")
