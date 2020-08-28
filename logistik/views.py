from logistik import app
from flask import render_template


@app.route("/hello/<name>")
@app.route("/hello")
def index(name):
    return render_template("index.html", name=name)
