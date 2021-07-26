from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField('Task', max_length=50)
    completed = models.BooleanField('Completed', default=False)
    created = models.DateTimeField('Created', auto_now_add=True)

    def __str__(self):
        return self.title


class Note(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default=1)
    title = models.CharField('Note', max_length=50)
    description = models.TextField('Description', null=True, blank=True)
    completed = models.BooleanField('Completed', default=False)
    created = models.DateTimeField('Created', auto_now_add=True)

    def __str__(self):
        return self.title
