from flask import render_template
from logistik import app


@app.route("/")
def dashboard():
    return render_template("dashboard/dashboard.html")
