from django.views import View
from django.shortcuts import render
from project.project_service import ProjectService



class DetailProjectView(View):
    def get(self, request, pk: int):
        project = ProjectService().get_project(pk)
        return render(
            request, 
            'project/detail_project.html', 
            context={"project": project}
        )




