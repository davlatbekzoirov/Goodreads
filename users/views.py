from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from .forms import UserCreateForm, UserLoginForm

class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form
        }
        return render(request, "users/register.html", context=context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()

            return redirect('users:login')
        else:
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context=context)

class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()

        context = {
            "login_form": login_form,
        }
        return render(request, "users/login.html", context)

    def post(self, request):
        login_form = UserLoginForm(data=request.POST)

        if login_form.is_valid():
            pass
        else:
            context = {
                "login_form": login_form,
            }
            return render(request, "users/login.html", context)
