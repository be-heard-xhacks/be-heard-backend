from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI']=os.environ['URI']
mongo = PyMongo(app)
db = mongo.db

@app.route("/", methods = ['GET'])
def hello():
    return "Our backend server!"
