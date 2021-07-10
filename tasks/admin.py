from django.contrib import admin
from .models import Note, Task

admin.site.register(Note)
admin.site.register(Task)