from flask import Flask
from api import routes

import firebase

app = Flask(__name__)
app.config["DEBUG"] = True
firebase_app = firebase.FirebaseApp()

app.register_blueprint(routes.firebase_api)


if __name__ == '__main__':
    app.run()
