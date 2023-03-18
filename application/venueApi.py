from flask_restful import Resource, marshal_with
from application.database import db
from application.models import Bookings, Venues, Shows
from application.validate import NotFoundError, ShowAtVenueError, VenueCreationError
from application.parsers import (
    create_show_parser,
    update_show_parser,
    create_venue_parser,
    update_venue_parser,
)
from application.marshal_formats import venue_output, show_output


class VenueAPI(Resource):
    @marshal_with(venue_output)
    def get(self, venueID):
        venue = db.session.query(Venues).filter(Venues.ID == venueID).first()
        if venue:
            return venue
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(venue_output)
    def put(self, venueID):
        venue = db.session.query(Venues).filter(Venues.ID == venueID).first()
        if venue:
            pass
        else:
            raise NotFoundError(status_code=404)

        args = update_venue_parser.parse_args()
        Name = args.get("Name", str)

        if Name is None:
            raise VenueCreationError(status_code=405, status_message="Name is required", error_code="VU1001")
        elif db.session.query(Venues).filter(Venues.Name == Name).first():
            raise VenueCreationError(
                status_code=400, status_message="Same Name Venue Exists", error_code="VU1002"
            )
        else:
            venue.Name = Name
            db.session.add(venue)
            db.session.commit()
            return venue, 200

    def delete(self, venueID):
        venue = db.session.query(Venues).filter(Venues.ID == venueID).first()
        if venue:
            shows = db.session.query(Shows).filter(Shows.Venue_ID == venueID).first()
            if shows:
                raise ShowAtVenueError(status_code=401)
            else:
                db.session.delete(venue)
        else:
            raise NotFoundError(status_code=404)
        
    @marshal_with(venue_output)
    def post(self):
        args = create_venue_parser.parse_args()
        Name = args.get("Name", str)
        Place = args.get("Place", str)
        City = args.get("City", str)
        Capacity = args.get("Capacity", int)

        if Name is None:
            raise VenueCreationError(status_code=400, status_message="Name is required", error_code="VC1001")
        elif Place is None:
            raise VenueCreationError(status_code=400, status_message="Place is required", error_code="VC1002")
        elif City is None:
            raise VenueCreationError(status_code=400, status_message="City is required", error_code="VC1003")
        elif Capacity is None:
            raise VenueCreationError(status_code=400, status_message="Capacity is required", error_code="VC1004")
        else:
            venue = Venues(Name=Name, Place=Place, City=City, Capacity=Capacity)
            db.session.add(venue)
            db.session.commit()
            return venue


class UserAPI(Resource):
    def get(self, userID, showID):
        pass

    def put(self, userID, showID):
        pass

    def delete(self, userID, showID):
        pass

    def post(self):
        pass
