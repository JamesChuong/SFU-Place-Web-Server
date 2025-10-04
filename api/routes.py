from flask import Blueprint, request

firebase_api = Blueprint('data', __name__)


@firebase_api.get()
def get_data():
    return "Hello World"
