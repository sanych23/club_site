from django.views import View
import pprint
from project.forms import ProjectCreateForm
from django.shortcuts import redirect, render
from project.dtos.request.create_project_dto import CreateProjectDTO
# from django.contrib.auth.decorators import login_required
from project.project_service import ProjectService



class ProjectCreateView(View):
    def get(self, request):
        return render(
            request, 
            'project/create_project.html', 
            context={'form': ProjectCreateForm()}
        )


    def post(self, request):
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            data = CreateProjectDTO(**form.cleaned_data, author_id=request.user.id)
            ProjectService().create_project(data)
            return redirect('list_project')
        return redirect('create_project')


