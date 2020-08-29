from functools import wraps
from flask import request, redirect, url_for
from logistik.models import User


def login_required(view):
    '''A decorator to redirct the user to the login page if not logged in'''
    @wraps(view)
    def wrapper(*args, **kwargs):
        name = request.cookies.get('user')
        if name is None or User.query.filter_by(name=name).first() is None:
            return redirect(url_for('login'), 302)
        return view(*args, **kwargs)
    return wrapper

from . import index
from . import auth
