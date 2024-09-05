from django import forms
from models.enums import Status, Role, Grade
from models.stack import Stack


class ProjectCreateForm(forms.Form):
    def __init__(self, *args, stacks=None, categories=None, **kwargs):
        super().__init__(*args, **kwargs)
        if stacks is not None:
            self.fields["stacks"] = forms.ModelMultipleChoiceField(
                queryset=stacks,
                required=True,
                # widget=forms.CheckboxSelectMultiple,
            )
        if categories is not None:
            self.fields["categories"] = forms.ModelMultipleChoiceField(
                queryset=categories,
                required=True,
                # widget=forms.CheckboxSelectMultiple,
            )


    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=5000)
    repo_link = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices=Status)
    author_role = forms.ChoiceField(choices=Role)
    deadline = forms.DateTimeField()
    categories = forms.ModelMultipleChoiceField(queryset=None)
    stacks = forms.ModelMultipleChoiceField(queryset=None)
    grade = forms.ChoiceField(choices=Grade)
    # vacancies = forms.

