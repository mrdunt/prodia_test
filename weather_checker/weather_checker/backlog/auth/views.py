from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from weather_checker.backlog.auth.forms import (
    LoginAuthForm)


def login_backlog(request):
    form = LoginAuthForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('backlog:weather_checking:index')
        else:
            messages.error(request, 'Email atau Sandi salah.')

    ctx = {'login_form': form}
    return render(request, 'auth/login.html', ctx)


def logout_backlog(request):
    logout(request)
    return redirect('backlog:auth:login')