from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import LoginForm, SignUpForm


def login_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})


def register_user(request: HttpRequest) -> HttpResponse:
    msg = None
    success = False

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'User created - please <a href="/login">login</a>.'
            success = True
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, 'accounts/register.html', {'form': form, 'msg': msg, 'success': success})
