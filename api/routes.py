from flask import Blueprint, request, jsonify
from api import auth
from firebase_admin import firestore
import uuid

firebase_api = Blueprint('firebase', __name__)

db = firestore.client()

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


@firebase_api.post("/sign_up")
def register_user():

    uid = str(uuid.uuid4())

    user_info = {
        "name": request.json["name"],
        "email": request.json["email"],
        "uid": uid,
    }

    user_ref = db.collection("users").document(uid)

    user_ref.set(user_info)

    return jsonify(user_info), 201

