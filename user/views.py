from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm
from .decorators import user_not_authenticated

# Create your views here.
@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="users/register.html",
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
        form = UserLoginForm(request=request, data = request.POST)
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
            for key, error in list(form.errors.values()):
                if key == 'captcha' and error[0] == 'This field is required':
                    messages.error(request, "You must pass the reCAPTCHA test") 
                    continue
                messages.error(request, error)

    form = UserLoginForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
        )

def user_profile(request, username):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f"{user_form.email} Your profile has been update")
            return redirect('profile', user_form.email)
        
        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user :
        form = UserUpdateForm(instance=user)
        return render(
            request=request,
            template_name="users/profile.html",
            context={"form": form}
        )
    return redirect("homepage")