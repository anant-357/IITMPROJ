from application.models import Users
from werkzeug.exceptions import HTTPException
from flask import make_response
import json

def isValidUser(user_name, password, isAdmin):
    users = Users.query.all()
    for user in users:
        if user.UserName == user_name and user.Password == password and isAdmin and user.Admin == 1:
            return True
        elif user.UserName == user_name and user.Password == password and not isAdmin and user.Admin != 1:
            return True
    return False

class NotFoundError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('',status_code)

class ShowAtVenueError(HTTPException):
    def __init__(self, status_code, status_message):
        self.response = make_response(status_message,status_code)

class VenueCreationError(HTTPException):
    def __init__(self, status_code, status_message, error_code):
        error = {
            "error-code": error_code,
            "error-message": status_message
        }
        self.response = make_response(json.dumps(error), status_code)



