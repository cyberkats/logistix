from logistik import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    status_id = db.Column(db.Integer, db.FOreinKey('status.id'), nullable=False)

    def __repr__(self):
        return f'User {self.name}'


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    users = db.relationship('User', backref='role', lazy=True)


class Assets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    location = db.Column(db.Integer, db.ForeignKey(
        'location.id'), nullable=False)
    asset_type = db.Column(db.Integer, db.ForeignKey(
        'asset_type.id'), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)


class Asset_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    type_of_asset = db.Column(db.String(), nullable=False)
    assets = db.relationship('Asset', backref='asset_type', lazy=True)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitiude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    assets = db.relationship('Asset', backref='location', lazy=True)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    change_time = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    note = db.Column(db.String(), nullable=True)
    assets = db.relationship('Asset', backref='status', lazy=True)
    users = db.relationship('User', backref='satus', lazy=True)
