from django.core.signals import request_started
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import *
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

class IndexViews(View):
    def get(self, request):
        if request.user.is_authenticated:
            tasks = Task.objects.filter(owner=request.user).order_by('-status', '-deadline')
            context = {
                'status_choices': StatusChoise.choices,
                'tasks': tasks,
            }

            return render(request, 'index.html', context)
        return redirect('/login/')
    def post(self, request):
        Task.objects.create(
            title=request.POST['title'],
            detail=request.POST['details'],
            status=request.POST['status'],
            deadline=request.POST['deadline'] if request.POST['deadline'] else None,
            owner=request.user,
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

class SignUpView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.POST.get('password') == request.POST.get('confirm_password'):
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            if user is not None:
                return HttpResponse("Username band ")
            else:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                )
                login(request, user)
                return redirect('home')
        else:
            return self.get(request)

def logout_view(request):
    logout(request)
    return redirect('/login/')

class LogInView(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is  not  None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')