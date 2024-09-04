from django.db import models


class Status(models.TextChoices):
        OPEN = 'OPEN', 'Open'
        CLOSED = 'CLOSED', 'Closed'
        STARTED = 'STARTED', 'Started'
        BACKLOG = 'BACKLOG', 'Backlog'

class Role(models.TextChoices):
    BACKEND = 'BACKEND', 'Backend'
    FRONTEND = 'FRONTEND', 'Frontend'
    FULLSTACK = 'FULLSTACK', 'Fullstack'
    DESIGN = 'DESIGN', 'Design'
    DEVOPS = 'DEVOPS', 'Devops'
    QA = 'QA', 'Qa'
    PM = 'PM', 'Pm'
    OTHER = 'OTHER', 'Other'

class Grade(models.TextChoices):
    INTERN = 'INTERN', 'Intern'
    JUNIOR = 'JUNIOR', 'Junior'
    JUNIOR_PLUS = 'JUNIOR_PLUS', 'Junior+'
    MIDDLE = 'MIDDLE', 'Middle'
    MIDDLE_PLUS = 'MIDDLE_PLUS', 'Middle+'
    SENIOR = 'SENIOR', 'Senior'
    SENIOR_PLUS = 'SENIOR_PLUS', 'Senior+'
    LEAD = 'LEAD', 'Lead'

