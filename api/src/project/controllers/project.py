from django.views import View
from django.shortcuts import render


class ProjectView(View):
    def get(self, request):
        return render(request, 'project/list_projects.html', context={})




