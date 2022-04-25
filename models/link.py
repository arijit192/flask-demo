from database import links_collection
from flask import request,make_response

class Link():
    def __init__(self,link="",path="",email=""):
        self.link = link
        self.path = path
        self.email = email

    def create(self):
        links_collection.insert_one({"email":self.email,"link":self.link,"path":self.path})

    def find(self):
        if links_collection.count_documents({"path":self.path}):
            result = links_collection.find_one({"path":self.path})
            return result["link"]
        else:
            return "404"