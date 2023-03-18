from flask_restful import Resource, marshal_with
from application.database import db
from application.models import Shows
from application.validate import NotFoundError, BookedShowError, ShowCreationError
from application.parsers import create_show_parser, update_show_parser
from application.marshal_formats import show_output


class ShowAPI(Resource):
    @marshal_with(show_output)
    def get(self, showID):
        show = db.session.query(Shows).filter(Shows.ID == showID).first()
        if show:
            return show
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(show_output)
    def put(self, showID):
        show = db.session.query(Shows).filter(Shows.ID == showID).first()
        if show:
            pass
        else:
            raise NotFoundError(status_code=404)

        args = update_show_parser.parse_args()
        Name = args.get("Name", str)

        if Name is None:
            raise ShowCreationError(
                status_code=405, status_message="Name is required", error_code="SU1001"
            )
        elif db.session.query(Shows).filter(Shows.Name == Name).first():
            raise ShowCreationError(
                status_code=400,
                status_message="Same Name Show Exists",
                error_code="SU1002",
            )
        else:
            show.Name = Name
            db.session.add(show)
            db.session.commit()
            return show, 200

    def delete(self, showID):
        show = db.session.query(Shows).filter(Shows.ID == showID).first()
        if show:
            shows = db.session.query(Shows).filter(Shows.Show_ID == showID).first()
            if shows:
                raise BookedShowError(status_code=401)
            else:
                db.session.delete(show)
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(show_output)
    def post(self):
        args = create_show_parser.parse_args()
        Name = args.get("Name", str)
        VenueID = args.get("VenueID", int)
        Rating = args.get("Rating", str)
        Tag = args.get("Tags", str)
        TicketPrice = args.get("TicketPrice", int)
        Date_Time = args.get("Date_Time", str)

        if Name is None:
            raise ShowCreationError(
                status_code=400, status_message="Name is required", error_code="VC1001"
            )
        elif VenueID is None:
            raise ShowCreationError(
                status_code=400, status_message="Venue is required", error_code="VC1002"
            )
        elif Rating is None:
            Rating = 0
        elif Tag is None:
            raise ShowCreationError(
                status_code=400, status_message="Tag is required", error_code="VC1003",
            )
        elif TicketPrice is None:
            raise ShowCreationError(
                status_code = 400 ,status_message="Ticket Price is required", error_code="VC1004",
            )
        elif Date_Time is None:
            raise ShowCreationError(
                status_code = 400 ,status_message="Time of show is required", error_code="VC1005",
            )
        else:
            show = Shows(Name=Name, VenueID = VenueID, Rating = Rating, Tag = Tag)
            db.session.add(show)
            db.session.commit()
            return show
