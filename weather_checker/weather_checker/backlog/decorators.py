from typing import Callable, Any

from functools import wraps

from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse
from django.shortcuts import redirect


def login_required(view_func: Callable) -> Callable:
    @wraps(view_func)
    def decorator(request, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            messages.info(request, 'Please login as a user with privileges to view this page.')
            return redirect_to_login(request.path_info)
        return view_func(request, *args, **kwargs)
    return decorator