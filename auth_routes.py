from datetime import date
import os
import datetime
from route_config import *
from flask import Flask, jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from bson.objectid import ObjectId
import jwt
import datetime
# function to wrap around our db calls around

def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_token = None
        if 'access-token' in request.headers:
            auth_token = request.headers['access-token']
        
        if not auth_token:
            return jsonify({'message' : 'no auth token'})
        try:
            jwt_data = jwt.decode(auth_token, os.environ.get("PASSWORD_SALT"), algorithms=["HS256"])
            current_user = db.users.find_one({"_id": ObjectId(jwt_data['_id']) })
        except:
            return jsonify({"message": 'token is invalid'})
        return f(current_user, *args, **kwargs)
    return decorator

# print("Password salt is: " +os.environ.get("PASSWORD_SALT") )

# @app.route('/register', methods = ['POST'])
# def signup_user():
#     data


@app.route("/getBobert", methods = ['GET'])
def hello_bobert():
    return jsonify({"message": db.users.find_one({"email": "bobert"})["_id"]}) 





