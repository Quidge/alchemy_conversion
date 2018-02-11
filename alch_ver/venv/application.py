import os

from time import gmtime, strftime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/register", methods=["GET, POST"])
def register():
	"""Register user"""

	session.clear()

	error = None

	if request.method == "POST":

        if not request.form.get("username") or not request.form.get("password") or not request.form.get("confirmation"):
            error = "Missing fields"
            flash(error)
            return render_template("register.html", error=error)
        elif request.form.get("password") != request.form.get("confirmation"):
            error = "Passwords do not match"
            flash(error)
            return render_template("register.html", error=error)

        # if this logic passes, all fields must be filled in and
        # password matches confirmation

        # for brevity
        username = request.form.get("username")
        ptpass = request.form.get("password")

        












