from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


class tasklistview(ListView):
    model=Task
    template_name = 'task_detail_and_create.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()  # Add the form to the context
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    success_url = '/cbvhome/'  #

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('cbvhome')



def task_detail_and_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_detail_and_create')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'task_detail_and_create.html', {'form': form, 'tasks': tasks})
def task_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_detail_and_create')

    return render(request, 'task_detail_and_create.html', {'task': task})
def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail_and_create')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_update.html', {'form': form})
