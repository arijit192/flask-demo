from flask import request
from main import app
from models.user import User

@app.route("/login",methods=["POST"])
def user_login():
    print(request.json)
    user = User(name="",email=request.json["email"],password=request.json["password"])
    result = user.checkCreds()
    print(result)
    return result