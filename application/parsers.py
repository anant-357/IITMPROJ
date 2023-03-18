from flask_restful import reqparse

create_venue_parser = reqparse.RequestParser()
create_venue_parser.add_argument("Name",type = str)
create_venue_parser.add_argument("Place",type = str)
create_venue_parser.add_argument("City",type = str)
create_venue_parser.add_argument("Capacity",type = int)

update_venue_parser = reqparse.RequestParser()
update_venue_parser.add_argument("Name",type = str)
update_venue_parser.add_argument("Place",type = str)
update_venue_parser.add_argument("City",type = enumerate)
update_venue_parser.add_argument("Capacity",type = int)

create_show_parser = reqparse.RequestParser()
create_show_parser.add_argument("Name",type = str)
create_show_parser.add_argument("VenueID",type = int)
create_show_parser.add_argument("City",type = enumerate)
create_show_parser.add_argument("Capacity",type = int)

update_show_parser = reqparse.RequestParser()
update_show_parser.add_argument("Name",type = str)
update_show_parser.add_argument("Place",type = str)
update_show_parser.add_argument("City",type = enumerate)
update_show_parser.add_argument("Capacity",type = int)