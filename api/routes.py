from flask import Blueprint, request, jsonify
from api import auth
firebase_api = Blueprint('data', __name__)


@firebase_api.get("/")
def get_data():
    return "Hello World"


@firebase_api.get("/user_data")
@auth.authenticate_token
def get_user_data():

    user_info = {
        "uid": request.json["uid"],

        "name": request.json["name"],
        "email": request.json["email"],

    }

    return jsonify(user_info)

