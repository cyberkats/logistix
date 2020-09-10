from flask import render_template
from logistik import app


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard/dashboard.html")


@app.route("/new_asset")
def new_asset():
    return render_template("dashboard/new_asset.html")
