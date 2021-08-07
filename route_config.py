from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI']=os.environ['URI']
mongo = PyMongo(app)
db = mongo.db

@app.route("/", methods = ['GET'])
def hello():
    return "Our backend server!"

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

@app.route("/updateInterests", methods = ["POST"])
def updateInterests():
    objID = request.args.get("_id")
    if not objID:
      return "error: missing id"
    print(db.users.find_one({"_id": ObjectId(objID)}))
    interests = request.args.get("interests")
    query = {"_id": ObjectId(objID)}
    newval = {"$set": {"interests" : interests}}
    db.users.update_one(query,newval)
    return jsonify({'interests': db.users.find_one({"_id": ObjectId(objID)})['interests']})