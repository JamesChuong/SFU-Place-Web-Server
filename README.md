# SFU Place Web Server
The central server used for the SFU Place mobile app

Built with Flask and Firebase, using the Realtime Database and 
Firestore services

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
