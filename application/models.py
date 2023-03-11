from .database import db


class Venues(db.Model):
    __tablename__ = "VENUES"
    ID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Name = db.Column(db.String, unique=True)
    Place = db.Column(db.String)
    Capacity = db.Column(db.Integer)


class Shows(db.Model):
    __table__name = "SHOWS"
    ID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Venue_ID = db.Column(db.Integer, db.ForeignKey("VENUES.ID"))
    Name = db.Column(db.String, unique=True)
    Rating = db.Column(db.Integer)
    Tags = db.Column(db.String)
    TicketPrice = db.Column(db.Integer)
