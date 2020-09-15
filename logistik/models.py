from logistik import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'User {self.name}'


class AssetType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitiude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    note = db.Column(db.String(), nullable=True)


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    location = db.Column(db.Integer, db.ForeignKey(
        'location.id'), nullable=True)
    asset_type = db.Column(db.Integer, db.ForeignKey(
        'asset_type.id'), nullable=True)
