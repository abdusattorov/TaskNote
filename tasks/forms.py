from django import forms
from . import models


class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'completed']


class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title', 'description', 'completed']
