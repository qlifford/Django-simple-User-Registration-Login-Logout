from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def home(request):
    context = {}
    return render(request, 'home/home.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'registration/register.html', {'form': form})

# def login_user(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         password = request.POST['password1']
#         user = authenticate(request, name=name, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#     return render(request, 'registration/login.html')

def logouts(request):
    logout(request)
    return redirect('home')