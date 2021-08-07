from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello():
    return "Our backend server!"

    
