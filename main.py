from flask import Flask,request,make_response,render_template,redirect
from flask_bcrypt import Bcrypt
from models.link import Link

app = Flask(__name__)
bcrypt = Bcrypt(app)

import routes.user_registration
import routes.user_login
import routes.create_url

@app.route("/<path>",methods=["GET"])
def index(path):
    link = Link(path=path)
    site = link.find()
    return redirect(site)

@app.route("/",methods=["GET","POST"])
def starter():
    return make_response({"msg":"Welcome to Flask application"})

@app.route("/404",methods=["GET","POST"])
def not_found():
    return make_response({"msg":"Link not found"},404)
    

@app.route("/test/<name>",methods=["GET"])
def test(name):
    return make_response(render_template("index.html",name=name))

@app.route("/form",methods=["POST"])
def form_submit():
    if request.content_type == "application/json":
        print(request.json)
        return request.json
    else:
        print(request.form)
        return request.form