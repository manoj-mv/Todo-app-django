from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.forms import ModelForm
from django.urls import reverse_lazy

from .models import task

# Create your views here.

# class IndexView(ListView):
#     model=task

class CreateTask_and_list(CreateView):
    template_name='tasks/task_list.html'
    model=task
    fields=['title']
    success_url=reverse_lazy('tasks:create_and_list')

    # additional context for listing all tasks
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context["task_list"] = self.model.objects.all()
        return context

class updateTask(UpdateView):
    model=task
    fields='__all__'
    success_url=reverse_lazy('tasks:create_and_list')

class deleteTask(DeleteView):
    model=task
    success_url=reverse_lazy('tasks:create_and_list')
    



