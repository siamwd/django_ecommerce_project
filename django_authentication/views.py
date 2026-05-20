from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from .forms import LoginForm, RegisterForm


# def HomeView(TemplateView, LoginRequiredMixin):
#     template_name = 'django_authentication/home.html'
#     login_url = '/login/'
    
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'django_authentication/home.html'
    login_url = '/login/' 

def login_view(request):
    form = LoginForm()
    msg = ""

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username_or_email, password=password)

            if user:
                login(request, user)
                return redirect("django_authentication:home")  # Change as your URL name
            else:
                msg = "Invalid credentials, Please try again."

    return render(request, "django_authentication/login.html", {"form": form, "msg": msg})
def logout_view(request):
    logout(request)
    return redirect("django_authentication:login")
User = get_user_model()
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('django_authentication:login')  # Register হয়ে login page এ যাবে
    else:
        form = RegisterForm()

    return render(request, "django_authentication/register.html", {"form": form})
# Create your views here.
