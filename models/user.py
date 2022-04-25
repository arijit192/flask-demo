from database import users_collection
from main import bcrypt
from flask import make_response
import jwt
from helper.token import verify_token, create_token

SECRET = "thisissecretforjwt"

class User():
    def __init__(self,name="",email="",password=""):
        self.name = name
        self.email = email
        self.password = password
    
    def create(self):
        hash = bcrypt.generate_password_hash(self.password,12).decode("UTF-8")
        if not users_collection.count_documents({"email":self.email}):
            users_collection.insert_one({"name":self.name,"email":self.email,"password":hash})
            return make_response({"msg":"User created"},201)
        else:
            return make_response({"msg":"User already exists"},200)

    def checkCreds(self):
        if users_collection.count_documents({"email":self.email}):
            user = users_collection.find_one({"email":self.email})
            result = bcrypt.check_password_hash(user["password"],self.password)
            if result:
                token = create_token({"email":self.email})
                return make_response({"access_token":token},200)
            else:
                return make_response({"msg":"Entered passoword is incorrect"},200)
        else:
            return make_response({"msg":"User doesn't exist"},200)
