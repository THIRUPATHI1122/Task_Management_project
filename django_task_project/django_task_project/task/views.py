from django.shortcuts import render,get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, TaskFilterForm


def task_list(request):
    form = TaskFilterForm(request.GET)
    tasks = Task.objects.all()

    if form.is_valid():
        priority = form.cleaned_data.get('priority')
        if priority:
            tasks = tasks.filter(priority=priority)

    return render(request, 'task/task_list.html', {'task': tasks, 'form': form})


def task_add(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'task/task_form.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'task/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task/task_confirm_delete.html', {'task': task})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})
