from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Task, Note
from . import forms


@login_required(login_url="/accounts/login/")
def home(request):
    tasks = Task.objects.filter(user=request.user)
    notes = Note.objects.filter(user=request.user)

    return render(request, 'tasks/tasks.html', {'tasks': tasks, 'notes': notes})


@login_required(login_url="/accounts/login/")
def TaskCreate(request):
    if request.method == "POST":
        form = forms.CreateTask(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('tasks:home')
    else:
        form = forms.CreateTask()

    return render(request, 'tasks/task-create.html', {'form': form})


@login_required(login_url="/accounts/login/")
def NoteCreate(request):
    if request.method == "POST":
        form = forms.CreateNote(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('tasks:home')
    else:
        form = forms.CreateNote()

    return render(request, 'tasks/note-create.html', {'form': form})
