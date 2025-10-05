from flask import Blueprint, request, jsonify
from api import authentication
from firebase_admin import firestore, auth, db

firebase_api = Blueprint('firebase', __name__)

firestore_db = firestore.client()
realtime_db = db

@firebase_api.get("/")
def get_data():
    return "Hello World"


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

        auth.delete_user(request.json["user_id"])

        return jsonify({"success": True}), 200

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@firebase_api.get("/surface/<surface_id>")
@authentication.authenticate_token
def add_surface(surface_id: str):

    surface_ref = f"surfaces/{surface_id}"

    surface = realtime_db.reference(surface_ref).get()

    if not surface:

        return jsonify({"error": "Surface not found"}), 400

    return jsonify({"surface": surface}), 200


@firebase_api.get("/surface/all")
# @authentication.authenticate_token
def get_all_surfaces():

    surfaces = realtime_db.reference("surfaces").get()

    return jsonify({"surfaces": surfaces}), 200


@firebase_api.post("/surface")
@authentication.authenticate_token
def add_surface_data():

    data = request.get_json()

    new_ref = realtime_db.reference("surfaces").push(data)

    uid = new_ref.key

    new_ref.update({"uid": uid})

    return {"surface": data}, 201


@firebase_api.get("/surface/<surface_id>strokes/user/<user_id>")
@authentication.authenticate_token
def get_user_strokes(surface_id: str, user_id: str):

    user_ref = f"surfaces/{surface_id}/users/{user_id}/strokes"

    strokes = realtime_db.reference(user_ref).get()

    if strokes is None:
        return {"error": "No strokes found"}, 404

    return {"strokes": strokes}, 200


@firebase_api.post("/surface/strokes/user")
# @authentication.authenticate_token
def add_strokes():
    data = request.get_json()

    surface_id = data.get("surface_id")
    user_id = data.get("user_id")
    user_name = data.get("name")
    stroke = data.get("stroke")

    user_ref = realtime_db.reference(f"surfaces/{surface_id}/users/{user_id}")

    # Will also append the user to the surface object, if not done already
    stroke_ref = user_ref.child("strokes").push(stroke)

    stroke_uid = stroke_ref.key
    stroke_ref.update({"uid": stroke_uid})

    # If the user hasn't painted on the surface yet
    if user_ref.get() is None:

        user_ref.update({
            "name": user_name,
            "uid": user_id
        })

    # Return the stroke with its UID for return value

    stroke["uid"] = stroke_uid

    return jsonify({
        "surface_id": surface_id,
        "user_id": user_id,
        "name": user_name,
        "stroke": stroke
    }), 201
