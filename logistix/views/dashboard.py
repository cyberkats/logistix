from flask import render_template, request, redirect, url_for, Blueprint
from logistix import db
from logistix.models import Asset, Location, Status
from logistix.views import login_required

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def redir():
    return redirect(url_for('dashboard.index'))


@dashboard.route('/dashboard')
@login_required
def index():
    assets = Asset.query.all()
    return render_template('dashboard/dashboard.html', assets=assets)


@dashboard.route('/new_asset')
@login_required
def new_asset():
    is_invalid = request.args.get('is_invalid', default=False, type=bool)
    return render_template('dashboard/new_asset.html', is_invalid=is_invalid)


@dashboard.route('/new_asset', methods=['POST'])
@login_required
def create_asset():

    description = request.form.get('description')
    try:
        default_location_lat = float(request.form.get('default_location_lat'))
        default_location_long = float(request.form.get('default_location_long'))
        current_location_lat = float(request.form.get('current_location_lat'))
        current_location_long = float(request.form.get('current_location_long'))
    except ValueError:
        return redirect(url_for('new_asset', is_invalid=True))

    status = request.form.get('status')

    default_location = Location(
        latitude=default_location_lat, longitude=default_location_long)
    current_location = Location(
        latitude=current_location_lat, longitude=current_location_long)
    status = Status(description=status)
    asset = Asset(description=description, status=status,
                  default_location=default_location, current_location=current_location)

    db.session.add(asset)
    db.session.commit()

    return redirect(url_for('new_asset', is_invalid=False))
