from flask import Flask, request, render_template, redirect
from models import Pet, db, connect_db
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_default")
uri = os.getenv("DATABASE_URL", "postgresql:///adopt")
if uri.startswith("postgres://"):  # since heroku uses 'postgres', not 'postgresql'
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.debug = True

connect_db(app)

@app.before_first_request
def setup_table():
    """Creates the Pets table before the page is first accessed."""
    db.drop_all()
    db.create_all()

@app.route("/")
def display_home_page():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)