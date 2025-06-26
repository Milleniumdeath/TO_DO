from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import *
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class IndexViews(View):
    def get(self, request):
        tasks = Task.objects.order_by('-status', '-deadline')
        context = {
            'status_choices': StatusChoise.choices,
            'tasks': tasks,
        }

        return render(request, 'index.html', context)

    def post(self, request):
        Task.objects.create(
            title=request.POST['title'],
            detail=request.POST['details'],
            status=request.POST['status'],
            deadline=request.POST['deadline'] if request.POST['deadline'] else None,
        )
        return self.get(request)

class TaskUpdateViews(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        context ={
            'task': task,
            'status_choices': StatusChoise.choices,
        }
        return render(request, 'edit.html', context)

    def post(self, request, pk):

        task = get_object_or_404(Task, pk=pk)
        task.title = request.POST['title']
        task.detail = request.POST['details']
        task.status = request.POST['status']
        task.save()

        return redirect('home')

class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('home')
