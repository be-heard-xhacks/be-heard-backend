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

validParams = ['interests', 'email', 'password', 'firstName', 'lastName']
@app.route("/getUser", methods = ["GET"])
@auth_required
def getUser(uid):
    objID = ObjectId(uid)
    if not objID:
      return make_response(jsonify({'message' : 'missing uid'}), 404)

    user = db.users.find_one({"_id": objID})

    profile = {}
    for key in validParams:
      profile[key] = ''
      if key in user:
        profile[key] = user[key]
    
    return jsonify({'profile': profile})

@app.route("/updateUser", methods = ["POST"])
@auth_required
def updateUser(uid):
    objID = ObjectId(uid)
    if not objID:
      return make_response(jsonify({'message' : 'missing uid'}), 404)
    
    request_data = request.get_json()
    updatevals = {}
    for key in validParams:
      if key in request_data:
        updatevals[key] = request_data.get(key)
  
    user = db.users.find_one({"_id": objID})
    if not user:
      return make_response(jsonify({'message' : 'no user with that id'}), 404)

    for param in updatevals:
      # need to rehash the new password
      value = updatevals[param]
      if param == 'password':
        value = generate_password_hash(value, method = 'sha256')
      query = {"_id": objID}
      newval = {"$set": {param : value}}
      db.users.update_one(query, newval)
    
    return jsonify({'updated user': str(db.users.find_one({"_id": objID}))})

@app.route("/storeInfographic", methods = ["POST"])
@auth_required
def storeInfographic(uid):
  objID = ObjectId(uid)
  if not objID:
    return make_response(jsonify({'message' : 'missing uid'}), 404)
  request_data = request.get_json()
  request_sentences = request_data['sentences']
  request_title = request_data['title']
  db['user-content'].insert_one({
    'author': objID,
    'title': request_title,
    'sentences': request_sentences,
  })
  
  return jsonify({'message': "Stored Infographic"})

#@app.route("/getSpotlighted", methods = ["POST"])


  


