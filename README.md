# SFU Place Web Server
The central server used for the SFU Place mobile app

Built with Flask and Firebase, using the Realtime Database and 
Firestore services

### Firebase Setup

To set up Firebase for local use, follow these guides to create a separate Firebase app for this 
server:
- [Getting started with the Firebase Realtime Database on the web
](https://www.youtube.com/watch?v=pP7quzFmWBY)
- [Official Firebase Realtime Database Docs](https://firebase.google.com/docs/database/web/start)
- [Official Firebase Firestore Docs](https://firebase.google.com/docs/firestore/quickstart)

Create a `.env` file in your root directory with all the environment variables needed for 
Firebase (see the `app.py` and `firebase.py` files)

### Server Setup

```
# Clone the repo
git clone git@github.com:JamesChuong/SFU-Place-Web-Server.git

# This server was tested on Python 3.12, a virtual environment is also recommended

# Virtual Environment Setup (Assuming you are in the root directory of the repo)
python3 -m venv <venv_name>

# Activating the virtual environment (Linux/MacOS)
source <venv_name>/bin/activate

# Activating the virtual environment (Windows)
<venv_name>/Scripts/Activate

# Installing requirements
pip install -r requirements.txt

# Starting the server
flask run
# Or 
python3 app.py
```

### API Guide

API Guide is localed in the [development.md](/docs/development.md) file
