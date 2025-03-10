from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect("users:login")
    else:
        form = UserCreationForm()
    
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("home")
        messages.error(request, "Invalid username or password.")
    
    else:
        form = AuthenticationForm()
    
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("users:login")

@login_required
def profile_view(request):
    return render(request, "users/profile.html")
