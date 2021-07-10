from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.home, name="home"),
    path('task-create/', views.TaskCreate, name="task-create"),
    path('note-create/', views.NoteCreate, name="note-create"),
]
