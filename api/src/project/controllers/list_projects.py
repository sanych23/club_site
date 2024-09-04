from django.views import View
from django.shortcuts import render
from project.project_service import ProjectService



class ProjectView(View):
    def get(self, request):
        projects = ProjectService().list_projects()
        return render(
            request, 
            'project/list_projects.html', 
            context={"projects": projects}
        )




