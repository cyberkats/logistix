from logistik import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    status_id = db.Column(db.Integer, db.ForeignKey('status.id'),
                          nullable=False)
    status = db.relationship('Status')

    default_location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    default_location = db.relationship('Location',
                                       foreign_keys=default_location_id)

    current_location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    current_location = db.relationship('Location',
                                       foreign_keys=current_location_id)
