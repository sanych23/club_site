from django import forms
from models.enums import Status, Role


class ProjectCreateForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=5000)
    repo_link = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices=Status)
    author_role = forms.ChoiceField(choices=Role)
    deadline = forms.DateTimeField()
    

