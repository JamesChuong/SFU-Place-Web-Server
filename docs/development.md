# API Guide

## Database Guide
The server stores objects in the database as JSON, the two main objects stored are users for login and keeping
track of brush strokes, and surfaces which users draw onto:
    
    # Users are stored in Firestore
    - Users 
        - uid: String
        - email: String
        - name: String
    
    # Surfaces are stored in the Realtime Database service
    -Surface
        - uid: String
        - center: JSON
            - x: Number
            - y: Number
            - z: Number
        - extent: JSON
            - x: Number
            - y: Number
        - normal: JSON
            - x: Number
            - y: Number
            - z: Number
        -users: [] # List of users which have drawn on the surface
            - uid: String
            - name: String
            - strokes: [] # List of brush strokes made on the surface
                - color: String
                - x: Number
                - y: Number
                - z: Number

### Example Surface:

```
{
    "surfaces": [
        {
            "center": {
                "x": 30,
                "y": 50,
                "z": 60
            },
            "extent": {
                "x": 50,
                "y": 20
            },
            "normal": {
                "x": 10,
                "y": 20,
                "z": 40
            },
            "uid": "-OanFXJPJhiGI6-s5CM4",
            "users": [
                {
                    "name": "Bob",
                    "strokes": [
                        {
                            "color": "Blue",
                            "uid": "-OanFrXG8guAftAFqzmA",
                            "x": 30,
                            "y": 50,
                            "z": 50
                        }
                    ],
                    "uid": "9zbJtDXnQxcwKoUHJnAeH6vU7Xb2"
                }
            ]
        }
    ]
}
```

## API Endpoint Guide

### Authentication

The server will only verify ID tokens for API endpoints and handle user registration, login is handled by
the native mobile app

Certain endpoints have a `@authentication.authenticate_token` decorator which verifies if the ID token in the request
is valid

#### POST /register
```
# Registers user in app

# Example Input:

{
    "name": "Benny",
    "email": "benny@example.ca",
    "password": "123456"
}

# Output:

{
    "email": "benny@example.ca",
    "name": "Benny",
    "uid": "Nsm9Gtfo2pbuRVTfHMeRDJEAUcG2"
}
```

#### DELETE /user/delete
```
# Deletes account

# Example Input:

{
    "user_id": "Nsm9Gtfo2pbuRVTfHMeRDJEAUcG2"
}

# Output:

{
    "success": true
}

```


### Uploading and Retrieving Data

#### GET /surface/<surface_id>

```
# Retrieves a surface with a specific ID

# Example URL:

http://127.0.0.1:5000/surface/-OanFXJPJhiGI6-s5CM4

# Output:

{
    "surface": [
        {
            "center": {
                "x": 30,
                "y": 50,
                "z": 60
            },
            "extent": {
                "x": 50,
                "y": 20
            },
            "normal": {
                "x": 10,
                "y": 20,
                "z": 40
            },
            "uid": "-OanFXJPJhiGI6-s5CM4",
            "users": [
                {
                    "name": "Bob",
                    "strokes": [
                        {
                            "color": "Blue",
                            "uid": "-OanFrXG8guAftAFqzmA",
                            "x": 30,
                            "y": 50,
                            "z": 50
                        }
                    ],
                    "uid": "9zbJtDXnQxcwKoUHJnAeH6vU7Xb2"
                }
            ]
        }
    ]
}
```

#### GET /surface/all

```
# Retrieves all surfaces in the DB

# Example output:

{
    "surfaces": [
        {
            "center": {
                "x": 30,
                "y": 50,
                "z": 60
            },
            "extent": {
                "x": 50,
                "y": 20
            },
            "normal": {
                "x": 10,
                "y": 20,
                "z": 40
            },
            "uid": "-OanFXJPJhiGI6-s5CM4",
            "users": [
                {
                    "name": "Bob",
                    "strokes": [
                        {
                            "color": "Blue",
                            "uid": "-OanFrXG8guAftAFqzmA",
                            "x": 30,
                            "y": 50,
                            "z": 50
                        }
                    ],
                    "uid": "9zbJtDXnQxcwKoUHJnAeH6vU7Xb2"
                }
            ]
        },
        {
            "center": {
                "x": 50,
                "y": 190,
                "z": 10
            },
            "extent": {
                "x": 30,
                "y": 100
            },
            "normal": {
                "x": 10,
                "y": 20,
                "z": 40
            },
            "uid": "-OanIfyyIGSjHujtG8aP"
        }
    ]
}
```

#### POST /surface

```
# Uploads a surface to the DB

# Example Input:

{
    "center": {
        "x": 50,
        "y": 190,
        "z": 10
    },
    "extent": {
        "x": 30,
        "y": 100
    },
    "normal": {
        "x": 10,
        "y": 20,
        "z":40
    },
    "users": []     # Field is optional
}
```

#### GET /surface/<surface_id>/user/<user_id>/strokes

```
# Retrieves all brush strokes made by a user on a surface

# Example URL:

http://127.0.0.1:5000/surface/-OanFXJPJhiGI6-s5CM4/user/9zbJtDXnQxcwKoUHJnAeH6vU7Xb2/strokes

# Example Output:

{
    "strokes": [
        {
            "color": "Blue",
            "uid": "-OanFrXG8guAftAFqzmA",
            "x": 30,
            "y": 50,
            "z": 50
        }
    ]
}
```

#### POST /surface/strokes/user

```
# Uploads a stroke to a specific surface

# Example Input:
{
    "surface_id": "-OanFXJPJhiGI6-s5CM4",
    "user_id": "9zbJtDXnQxcwKoUHJnAeH6vU7Xb2",
    "name": "Bob",
    "stroke": {
        "color": "Blue",
        "x": 30,
        "y": 50,
        "z": 50
    }
}
```