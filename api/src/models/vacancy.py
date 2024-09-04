from django.db import models
from .enums import Grade


class ProjectVacancy(models.Model):
    # name = models.CharField(max_length=255)
    # description = models.TextField()
    # salary = models.IntegerField()
    # company = models.ForeignKey('Company', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project_vacancies')
    stack = models.ForeignKey('Stack', on_delete=models.CASCADE, related_name='stack_vacancies')
    grade = models.CharField(choices=Grade, default=Grade.INTERN, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     return self.name
    
    class Meta:
        db_table = 'project_vacancies'
