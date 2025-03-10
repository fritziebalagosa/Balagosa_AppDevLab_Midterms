from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Task
from .forms import TaskForm
from django.db.models import Q

def task_create(request):
    if request.method == "POST":
        print(request.POST)  
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print("Task saved successfully!") 
            return redirect('task_list')
        else:
            print("Form errors:", form.errors)  
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()  # `status` will be set automatically
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
