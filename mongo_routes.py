from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from route_config import *

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
    
@app.route("/addUser", methods = ["POST"])
def addUser():
    print(request.args)
    emailInput = request.args.get("email")
    password = request.args.get("password")
    interests = request.args.get("interests")
    emailNum = db["users"].find({ "email": emailInput}).count()
    if (emailNum >0):
        print("Email already exists!")
        return ("error, email already exists!")
    newUser = db.users.insert_one({
        "email" : emailInput,
        "password" : password,
        "interests" : interests
    })
    
    print("Adding person of email: " + emailInput + " to db")
    return "Successfully added email of: " + emailInput

@app.route("/deleteUser", methods = ["POST"])
def deleteUser():
    nameInput = request.args.get("name")
    query = { "name": nameInput}
    result = db.users.delete_one(query)
    if (result.deleted_count == 0):
        return "User did not exist"
    else: 
        return ("Deleted user: " + nameInput)

@app.route("/getInterestsByID", methods = ["GET"])
def getInterestsByID():
    objID = request.args.get("_id")
    if not objID:
      return "error: missing id"
    print(db.users.find_one({"_id": ObjectId(objID)}))
    return jsonify({'interests': db.users.find_one({"_id": ObjectId(objID)})['interests']})

validParams = ['interests', 'email', 'password']
@app.route("/update<param>", methods = ["POST"])
def updateInterests(param):
    param = param.lower()
    if param not in validParams:
      return '404 invalid route'
    objID = request.args.get("_id")
    value = request.args.get("value")
    if not objID:
      return "error: missing id"
    user = db.users.find_one({"_id": ObjectId(objID)})
    print(user)
    if not user:
      return 'no user with that id'
    query = {"_id": ObjectId(objID)}
    newval = {"$set": {param : value}}
    db.users.update_one(query,newval)
    return jsonify({param: db.users.find_one({"_id": ObjectId(objID)})[param]})
