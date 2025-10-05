from flask import Blueprint, request, jsonify
from api import authentication
from firebase_admin import firestore, auth

firebase_api = Blueprint('firebase', __name__)

db = firestore.client()


@firebase_api.get("/")
def get_data():
    return "Hello World"


@firebase_api.get("/user_data")
@authentication.authenticate_token
def get_user_data():

    user_info = {
        "uid": request.json["uid"],
        "name": request.json["name"],
        "email": request.json["email"],

    }

    return jsonify(user_info)


@firebase_api.post("/register")
def register_user():

    try:

        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not all([name, email, password]):
            return jsonify({"error": "Missing name, email, or password"}), 400

        user = auth.create_user(
            email=email,
            password=password,
            display_name=name
        )

        user_info = {
            "name": name,
            "email": email,
            "uid": user.uid,
        }

        user_ref = db.collection("users").document(user.uid)

        user_ref.set(user_info)

        return jsonify(user_info), 201

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@firebase_api.delete("/delete_user")
@authentication.authenticate_token
def delete_user():

    try:

        auth.delete_user(request.json["uid"])

        return jsonify({"success": True}), 200

    except Exception as e:

        return jsonify({"error": str(e)}), 400
