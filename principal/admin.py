from django.contrib import admin

# Register your models here.

from .models import Project, Tasks

admin.site.register(Project)
admin.site.register(Tasks)