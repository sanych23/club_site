from .dtos.request.create_project_dto import CreateProjectDTO
from models.project import Project


class ProjectService:
    def create_project(self, dto: CreateProjectDTO) -> None:
        return Project.objects.create(**dto.__dict__)
        

