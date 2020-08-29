from logistik import app
from flask import render_template


@app.route("/hello/<name>")
@app.route("/hello")
def hello(name):
    return render_template("index.html", name=name)
