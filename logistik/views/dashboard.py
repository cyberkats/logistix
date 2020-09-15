from flask import render_template, request
from logistik import app, db
from logistik.models import Asset


@app.route("/dashboard")
def dashboard():
    assets = Asset.query.all()
    return render_template("dashboard/dashboard.html", assets=assets)


@app.route("/new_asset")
def new_asset():

    description = request.form.get('description')
    location = request.form.get('location')
    asset_type = request.form.get('asset_type')
    status = request.form.get('status')

    asset = Asset(description=description, location=location,
                  asset_type=asset_type, status=status)
    db.session.add(asset)
    db.session.commit()

    return render_template("dashboard/new_asset.html")
