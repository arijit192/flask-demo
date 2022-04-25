from flask import request
from main import app
from models.user import User

@app.route("/register",methods=["POST"])
def user_registration():
    print(request.json)
    user = User(request.json["name"],request.json["email"],request.json["password"])
    result = user.create()
    print(result)
    return result