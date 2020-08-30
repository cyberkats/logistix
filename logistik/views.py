from logistik import app
from flask import render_template


@app.route("/")
def map():
    return render_template("index.html", lat=-38.15, long=144.35)
