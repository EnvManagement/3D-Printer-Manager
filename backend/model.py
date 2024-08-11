from sqlalchemy.dialects.postgresql import ARRAY
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    firstname = db.Column(db.String(60))
    surname = db.Column(db.String(60))
    mail = db.Column(db.String(80))
    department = db.Column(db.String(60))

    admin = db.Column(db.Boolean)

    def json(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'surname': self.surname,
            'mail': self.mail,
            'department': self.department,
            'admin': self.admin}


class Printers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60))
    model = db.Column(db.String(60))
    image = db.Column(db.String(300))
    manufacturer = db.Column(db.String(60))
    bookings = db.Column(ARRAY(db.Integer))
    filaments = db.Column(ARRAY(db.Integer))

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'image': self.image,
            'manufacturer': self.manufacturer,
            'bookings': self.bookings,
            'filaments': self.filaments,
        }


class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(20), db.ForeignKey('users.id'))
    printer = db.Column(db.Integer, db.ForeignKey('printers.id'))
    start_time = db.Column('from', db.TIMESTAMP)
    end_time = db.Column('to', db.TIMESTAMP)

    def json(self):
        return {
            'id': self.id,
            'user': self.user,
            'printer': self.printer,
            'from': self.start_time,
            'to': self.end_time,
        }


class Filaments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.Column(db.String(60))
    material = db.Column(db.String(60))
    manufacturer = db.Column(db.String(60))
    approximate_left = db.Column(db.Float)

    def json(self):
        return {
            'id': self.id,
            'color': self.color,
            'material': self.material,
            'manufacturer': self.manufacturer,
            'approximate_left': self.approximate_left,
        }
