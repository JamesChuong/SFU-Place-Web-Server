from flask import Flask
import firebase
from dotenv import load_dotenv
import os

firebase_app = firebase.FirebaseApp()

from api import routes

load_dotenv()

app = Flask(__name__)
app.config["DEBUG"] = bool(os.getenv("DEBUG"))

app.register_blueprint(routes.firebase_api)

if __name__ == '__main__':
    app.run()
