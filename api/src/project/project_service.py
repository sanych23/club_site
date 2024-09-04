from .dtos.request.create_project_dto import CreateProjectDTO
# from models.project import Project
from .repository import ProjectRepository


class ProjectService:
    def __init__(self) -> None:
        self.repository = ProjectRepository()

    def create_project(self, dto: CreateProjectDTO) -> None:
        self.repository.create_project(dto)

    def list_projects(self):
        return self.repository.list_projects()
    
    def get_project(self, pk: int):
        return self.repository.get_project(pk)
