from django.views import View
import pprint
from project.forms import ProjectCreateForm
from django.shortcuts import redirect, render
from project.dtos.request.create_project_dto import CreateProjectDTO
from django.contrib.auth.mixins import LoginRequiredMixin
from project.project_service import ProjectService



class ProjectCreateView(LoginRequiredMixin,View):
    def get(self, request):
        return render(
            request, 
            'project/create_project.html', 
            context={'form': ProjectCreateForm()}
        )


    def post(self, request):
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            categories_str = form.cleaned_data.pop('categories')
            stacks_str = form.cleaned_data.pop('stacks')
            data = CreateProjectDTO(**form.cleaned_data, 
                                    author_id=request.user.id,
                                    categories=list(map(int, categories_str.split(','))),
                                    stacks=list(map(int, stacks_str.split(',')))
                                    )
            ProjectService().create_project(data)
            return redirect('list_project')
        return redirect('create_project')


