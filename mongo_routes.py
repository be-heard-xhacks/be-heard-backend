from bson.objectid import ObjectId
from route_config import *
from auth_routes import auth_required
from flask import jsonify, make_response
from werkzeug.security import generate_password_hash

@app.route("/getUsers", methods = ["GET"])
def getUsers():
    cursor = db.users.find({})
    usersList = []
    for doc in cursor:
        print(doc)
        usersList.append({
            "email" : doc["email"],
            "password" : doc["password"],
            "interests" : doc["interests"],
            "_id": str(doc["_id"])
        })
    #return the list of users
    print(usersList)
    return jsonify({ "users": usersList })

# @app.route("/deleteUser", methods = ["POST"])
# def deleteUser():
#     nameInput = request.args.get("name")
#     query = { "name": nameInput}
#     result = db.users.delete_one(query)
#     if (result.deleted_count == 0):
#         return "User did not exist"
#     else: 
#         return ("Deleted user: " + nameInput)

@app.route("/getInterests", methods = ["GET"])
@auth_required
def getInterests(uid):
    objID = ObjectId(uid)
    if not objID:
      return make_response(jsonify({'message' : 'missing uid'}), 404)
    print(db.users.find_one({"_id": objID}))
    return jsonify({'interests': db.users.find_one({"_id": objID})['interests']})

validParams = ['interests', 'email', 'password']
@app.route("/update<param>", methods = ["POST"])
@auth_required
def updateUser(uid, param):
    objID = ObjectId(uid)
    if not objID:
      return make_response(jsonify({'message' : 'missing uid'}), 404)
    param = param.lower()
    print(param)
    if param not in validParams:
      return make_response(jsonify({'message' : 'route not found'}), 404)
    
    value = request.args.get("value")
    # need to rehash the new password
    if param == 'password':
      value = generate_password_hash(value, method = 'sha256')

    user = db.users.find_one({"_id": objID})
    if not user:
      return make_response(jsonify({'message' : 'no user with that id'}), 404)
    query = {"_id": objID}
    newval = {"$set": {param : value}}
    db.users.update_one(query, newval)
    return jsonify({param: db.users.find_one({"_id": objID})[param]})
