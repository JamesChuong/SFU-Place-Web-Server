from flask import Flask
from api.routes import firebase_api

app = Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(firebase_api)


if __name__ == '__main__':
    app.run()