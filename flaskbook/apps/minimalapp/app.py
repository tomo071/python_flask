from email_validator import validate_email, EmailNotValidError

from flask import (
  Flask,  
  current_app, 
  g, 
  redirect,
  render_template,
  request, 
  url_for, 
  flash,
)

import logging

from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)

app.config["SECRET_KEY"]="2AZSMss3p5QPbcY2hBsJ"

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.logger.setLevel(logging.DEBUG)

toolbar = DebugToolbarExtension(app)

@app.route("/")
def index():
  return "Hello Flaskbook!"

@app.route("/hello/<name>",
 methods=["GET","POST"],
 endpoint="hello-endpoint")
def hello(name):
  return f"hello {name}!"
def show_name(name):
  return render_template("index.html", name=name)

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/contact/complete",methods=["GET","POST"])
def contact_complete():
  if request.method == "POST":

    username = request.form["username"]
    email = request.form["email"]
    description = request.form["description"]

    is_valid = True

    if not username:
      flash("ユーザー名は必須です")
      is_valid = False

    return redirect(url_for("contact_complete"))

  return render_template("contact_complete.html")

with app.test_request_context():
  print(url_for("index"))
  print(url_for("hello-endpoint", name="world"))
  print(url_for("show_name", name="name", page="1"))

with app.test_request_context("/users?updated=true"):
  print(request.args.get("updated"))

