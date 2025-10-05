from flask import Blueprint, request, jsonify
from api import authentication
from firebase_admin import firestore, auth, db

firebase_api = Blueprint('firebase', __name__)

firestore_db = firestore.client()
realtime_db = db

@firebase_api.get("/")
def get_data():
    return "Hello World"


@firebase_api.get("/user")
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

        user_ref = firestore_db.collection("users").document(user.uid)

        user_ref.set(user_info)

        return jsonify(user_info), 201

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@firebase_api.delete("/user/delete")
@authentication.authenticate_token
def delete_user():

    try:

        auth.delete_user(request.json["uid"])

        return jsonify({"success": True}), 200

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@firebase_api.get("/surface")
@authentication.authenticate_token
def add_surface():

    surface_id = request.json["uid"]
    surface_ref = f"surfaces/{surface_id}"

    surface = realtime_db.reference(surface_ref).get()

    if not surface:

        return jsonify({"error": "Surface not found"}), 400

    return jsonify({"surface": surface}), 200


@firebase_api.post("/surface")
@authentication.authenticate_token
def add_surface_data():

    data = request.get_json()

    realtime_db.reference("surfaces").push(data)

    return {data}, 201
