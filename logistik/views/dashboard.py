from datetime import datetime
from flask import render_template, request, redirect
from logistik import app, db
from logistik.models import Asset, Location, Status


@app.route("/dashboard")
def dashboard():
    assets = Asset.query.all()
    return render_template("dashboard/dashboard.html", assets=assets)


@app.route("/new_asset")
def new_asset():
    return render_template("dashboard/new_asset.html")


@app.route("/new_asset", methods=["POST"])
def create_asset():

    description = request.form.get('description')
    default_location_lat = request.form.get('default_location_lat')
    default_location_long = request.form.get('default_location_long')
    current_location_lat = request.form.get('current_location_lat')
    current_location_long = request.form.get('current_location_long')
    asset_type = request.form.get('asset_type')
    status = request.form.get('status')

    default_location = Location(
        latitude=default_location_lat, longitude=default_location_long)
    current_location = Location(
        latitude=current_location_lat, longitude=current_location_long)
    db.session.add(default_location)
    db.session.add(current_location)
    db.session.commit()

    status = Status(time=datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"), description=status)
    db.session.add(status)
    db.session.commit()

    asset = Asset(description=description, status=status.id,
                  default_location=default_location.id, current_location=current_location.id)

    db.session.add(asset)
    db.session.commit()

    return redirect("/new_asset")
