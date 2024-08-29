from django.apps import AppConfig


class ModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models'

    def ready(self):
        # from .user import CustomUser
        from models.project import Project
        from models.category import Category
        from models.stack import Stack
        # from .category import Category
        # from .stack import Stack
        # from .vacancy import ProjectVacancy

