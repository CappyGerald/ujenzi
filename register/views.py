from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
# Signup view


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_manager:dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/signup.html', {'form': form, 'show_image': False})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('project_manager:dashboard')
            else:
                return render(request, 'register/login.html', {'error': 'invalid login credentials', 'show_image': False})
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})

def custom_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('register:user_login')
    return redirect('project_manager:dashboard')