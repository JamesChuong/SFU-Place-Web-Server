from flask import Flask
import firebase
import dotenv
import os

firebase_app = firebase.FirebaseApp()

from api import routes


app = Flask(__name__)
app.config["DEBUG"] = os.getenv("DEBUG")

app.register_blueprint(routes.firebase_api)


if __name__ == '__main__':
    app.run()
