# from datetime import date
import os
import datetime
# from posix import environ
from route_config import *
from flask import jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from bson.objectid import ObjectId
import jwt
import datetime
# function to wrap around our db calls around

# TODO: USE IS_JSON and GETJSON
def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_token = None
        if 'access-token' in request.headers:
            auth_token = request.headers['access-token']
        if not auth_token:
            return make_response(jsonify({'message' : 'no auth token'}), 401)
        try:
            jwt_data = jwt.decode(auth_token, os.environ.get("PASSWORD_SALT"), algorithms=["HS256"])
            uid = ObjectId(jwt_data['_id'])
            db.users.find_one_or_404({"_id": uid})
        except:
            return make_response(jsonify({"message": 'token is invalid'}),401)
        return f(uid, *args, **kwargs)
    return decorator

# print("Password salt is: " +os.environ.get("PASSWORD_SALT") )

@app.route('/validateToken', methods = ['POST'])
def validate_token():     
    auth_token = request.headers['access-token']
    if request.is_json:
        auth_token = request.get_json().headers['access-token']
    try: 
        jwt_data = jwt.decode(auth_token, os.environ.get("PASSWORD_SALT"), algorithms=["HS256"])
        uid = ObjectId(jwt_data['_id'])
        user = db.users.find_one({"_id": uid})
    except:
        return make_response(jsonify({"message": 'token is invalid'}),401)
    if not user:
      return make_response(jsonify({"message": 'token is invalid'}), 401)
    return jsonify({"message": 'validation success'})

@app.route('/register', methods = ['POST'])
def registerUser():
    request_data = request.args
    if request.is_json:
        request_data = request.get_json()
    user_pass=request_data.get("password")
    user_email = request_data.get("email")

    prev_user = db.users.find_one( {"email": user_email})
    if prev_user:
        return jsonify({"message": "Error, email is taken"})

    hashed_password = generate_password_hash(user_pass, method = 'sha256')
    new_user = db.users.insert_one({
        "email": user_email,
        "password" : hashed_password
    })
    return jsonify({"message" : "User successfully registered" })

# why tf does this not work with jsons
@app.route('/login', methods = ['POST'])
def login_user():
    auth = request.authorization
    if request.is_json:
        print(request.get_json())
        auth = request.get_json()['authorization']
        # auth = request.get_json()['authorization']
    if not auth or not auth.username or not auth.password:
        return make_response(jsonify({ 'message': 'Invalid username or password'}),  401)
    print("auth.username is: " + auth.username)
    user = db.users.find_one_or_404({ "email" : auth.username})
    print(user)
    if check_password_hash(user["password"],auth.password):
        jwt_token = jwt.encode({ 
            '_id': str(user['_id']), 
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=4)
            },
            os.environ.get("PASSWORD_SALT"), "HS256")
        return jsonify({'jwt_token': jwt_token})
    return make_response(jsonify({ 'message': 'Invalid username or password'}),  401)
    


@app.route("/getGag", methods = ['GET'])
def hello_bobert():
    #gag = db.users.find_one({"email": "gag"})
    #print ("Gag is: " + db.users.find_one({"email": "gag"})["_id"])
    return jsonify({"message": str(db.users.find_one({"email": "gag"})["_id"])}) 



