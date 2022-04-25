from crypt import methods
from main import app
from models.link import Link
from flask import request,make_response
from helper.token import extract_token,verify_token,get_data
import jwt

@app.route("/createUrl",methods=["POST"])
def create_url():
    try:
        token_with_bearer = request.headers["authorization"]
    except:
        return make_response({"msg":"Authorization header is missing"})
    token_with_bearer = request.headers["authorization"]
    token = extract_token(token_with_bearer)
    if verify_token(token):
        data = get_data(token)
        link = Link(request.json["link"],request.json["path"],data["email"])
        link.create()
        return make_response({"msg":"Link has been created"},201)
    else:
        return make_response({"msg":"Token is invalid"},200)