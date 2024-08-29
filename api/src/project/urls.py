from django.urls import path
from .controllers import project, create_project

urlpatterns = [
    path('create/', create_project.ProjectCreateView.as_view(), name='create_project'),
    path('', project.ProjectView.as_view(), name='list_project'),
]

