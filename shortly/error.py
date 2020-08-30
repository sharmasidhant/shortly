from flask import Blueprint, jsonify, Response
from werkzeug.exceptions import HTTPException, InternalServerError

error = Blueprint('error', __name__)

@error.app_errorhandler(Exception)
def exceptionHandler(e):
    if isinstance(e, HTTPException):
        status_code = e.code
        error_message = e.description
    else:
        status_code = 500
        error_message = e.args[0] or "Something went wrong!"
    
    error = {
        "error": e.__class__.__name__,
        "code": status_code,
        "message": error_message
    }

    return jsonify(error), status_code
