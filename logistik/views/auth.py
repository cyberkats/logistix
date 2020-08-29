from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from sqlalchemy.exc import IntegrityError
from flask import render_template, request, redirect, make_response
from logistik import app, db
from logistik.models import User


@app.route('/login')
def login():
    '''Render the login page'''
    return render_template('auth/login.html', is_invalid=False)


@app.route('/login', methods=['POST'])
def authenticate():
    '''Check a post request form data with the User table'''
    ph = PasswordHasher()

    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(name=name).first()

    try:
        ph.verify(user.password, password)
        resp = make_response(redirect('/', 302))
        resp.set_cookie('user', str(user.name))
        return resp
    except (AttributeError, VerifyMismatchError):
        # Invalid user or password
        return render_template('auth/login.html', is_invalid=True)


@app.route('/new_user')
def new_user():
    '''Render the new user page'''
    return render_template('auth/new_user.html', is_taken=False, is_invalid=False)


@app.route('/new_user', methods=['POST'])
def create_user():
    '''Create a new user from a post request form'''
    ph = PasswordHasher()

    name = request.form.get('name')
    password = request.form.get('password')
    verify_password = request.form.get('verify_password')

    if password != verify_password:
        return render_template('auth/new_user.html', is_taken=False, is_invalid=True)

    user = User(name=name, password=ph.hash(password))
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        # User name already taken
        return render_template('auth/new_user.html', is_taken=True, is_invalid=False)

    return redirect('/login')
