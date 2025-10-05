from flask import Flask
import firebase

firebase_app = firebase.FirebaseApp()

from api import routes


app = Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(routes.firebase_api)


if __name__ == '__main__':
    app.run()
