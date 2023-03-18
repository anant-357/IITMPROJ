import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
import secrets
from flask_restful import Api
from flask_cors import CORS

app = None
api = None


def build_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv("ENV", "development") == "production":
        raise Exception("production config is not setup")
    else:
        print("Starting Local Deveopment Enviroment")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    secret = secrets.token_urlsafe(32)
    app.secret_key = secret
    CORS(app, resources={r"/*": {"origins": "*"}})
    return app, api


app, api = build_app()

from application.controllers import *

from application.api import UserAPI, VenueAPI

api.add_resource(UserAPI, "/api/user/booking/<bookingID>", "/api/user/booking")
api.add_resource(
    VenueAPI,
    "/api/admin/venue",
    "/api/admin/venue/<venueID>",
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
