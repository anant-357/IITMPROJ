from flask_restful import fields

venue_output = {
    "ID": fields.Integer,
    "Name": fields.String,
    "Place": fields.String,
    "City": fields.String,
    "Capacity": fields.Integer,
}

show_output = {
    "ID": fields.Integer,
    "Venue_ID": fields.Integer,
    "Name": fields.String,
    "Rating": fields.Integer,
    "Tags": fields.String,
    "TicketPrice": fields.Integer,
    "Date_Time": fields.DateTime,
}
