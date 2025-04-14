from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Task
from .forms import TaskForm
from django.contrib import messages


def task_list(request):
    query = request.GET.get('task_id')
    tasks = Task.objects.all().order_by('-due_date')

    if query:
        tasks = tasks.filter(id=query)

    return render(request, 'task/task_list.html', {'tasks': tasks})


def create_task(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Task added successfully!')
        return redirect('task_list')
    return render(request, 'task/task_form.html', {'form': form})


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task/task_form.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task/delete_confirm.html', {'task': task})


def dashboard(request):
    today = now().date()
    status = request.GET.get('status', 'all')

    all_tasks = Task.objects.all()
    tasks = all_tasks

    if status == 'pending':
        tasks = tasks.filter(is_completed=False)
    elif status == 'completed':
        tasks = tasks.filter(is_completed=True)

    total = all_tasks.count()
    completed = all_tasks.filter(is_completed=True).count()
    pending = all_tasks.filter(is_completed=False).count()
    overdue = all_tasks.filter(is_completed=True, due_date__lt=now()).count()
    completed_today = all_tasks.filter(due_date__date=today, is_completed=True).count()

    percent_done = round((completed / total) * 100, 2) if total else 0

    context = {
        'completed_today': completed_today,
        'pending': pending,
        'completed': completed,
        'overdue': overdue,
        'total': total,
        'percent_done': percent_done,
        'tasks': tasks,
        'status': status
    }

    return render(request, 'task/dashboard.html', context)

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect(request.META.get('HTTP_REFERER', 'task_list'))



