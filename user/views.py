from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Registration successful. {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error  (request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name = "users/register.html",
        context={"form": form}
    )

def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")

def custom_login(request):
    if request.user.is_authenticated:
        return redirect("homapage")
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data.get("username"),
                password = form.cleaned_data.get("password")
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Hello <b>{user.username}</b>')
                return redirect("homepage")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
        )
