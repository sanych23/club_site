# Generated by Django 5.0.7 on 2024-09-04 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_project_categories_project_stacks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('INTERN', 'Intern'), ('JUNIOR', 'Junior'), ('JUNIOR_PLUS', 'Junior+'), ('MIDDLE', 'Middle'), ('MIDDLE_PLUS', 'Middle+'), ('SENIOR', 'Senior'), ('SENIOR_PLUS', 'Senior+'), ('LEAD', 'Lead')], default='INTERN', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_vacancies', to='models.project')),
                ('stack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stack_vacancies', to='models.stack')),
            ],
        ),
    ]
