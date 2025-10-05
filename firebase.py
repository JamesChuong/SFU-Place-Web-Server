import json

import firebase_admin
from dotenv import load_dotenv
import os

from firebase_admin import credentials


class FirebaseApp:
    def __init__(self):
        load_dotenv()

        firebase_key_data = json.loads(os.getenv('FIREBASE_KEY'))

        firebase_config = credentials.Certificate(firebase_key_data)

        firebase_admin.initialize_app(firebase_config, {
            'databaseURL': os.getenv("FIREBASE_DATABASE_URL"),
        })



