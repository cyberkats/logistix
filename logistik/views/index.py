from flask import render_template
from logistik import app
from . import login_required


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
@app.route('/hello')
@login_required
def hello(name):
    return render_template('hello.html', name=name)
