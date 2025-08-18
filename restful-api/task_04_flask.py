#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}
@app.route("/")
def home():
    return "Welcome to the Flask API!"
@app.route("/data")
def datafn():
    return jsonify(list(users.keys()))

@app.route("/status")
def stat():
    return "OK",200

@app.route("/add_user",methods=["POST"])
def add_user():
    data =request.get_json()
    if "username" not in data:
        return {"error":"Username is required"},400
    users[data["username"]] = data 

    return {"message": "User added","user":data},201



@app.route("/users/<username>")
def user(username):
    if username in users.keys():
        return jsonify(users[username])
    else:
        return {"error": "User not found"},400

if __name__ == "__main__": app.run()