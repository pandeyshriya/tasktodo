from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import todo
from .forms import ListForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
#Add Django site authentication urls (for login, logout, password management)
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user:
            #log in th user
            login(request,user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Please enter valid credentials !!"
            return render(request, "TaskMan/home.html", context)
    else:
        return render(request,"TaskMan/home.html", context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))


def list_task(request):
    todos = todo.objects.all()
    return render(request, "task.html", {'todos':todos})


def create_task(request):
    form = ListForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, ("Item Has Been Added"))
        return redirect('list_task')

    return render(request, 'task_form.html', {'form': form})


def update_task(request, id):
    Todo = todo.objects.get(id=id)
    form = ListForm(request.POST or None, instance=Todo)

    if form.is_valid():
        form.save()
        return redirect('list_task')

    return render(request, 'task_form.html', {'form': form, 'todo':todo})



def delete_task(request, id):
    Todo = todo.objects.get(id=id)

    if request.method == 'POST':
        Todo.delete()
        return redirect('list_task')

    return render(request, 'task_delete.html', {'todo':todo})