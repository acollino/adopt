from flask import Flask, request, render_template, redirect
from models import Pet, db, connect_db
from forms import AddPetForm
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
    """Displays the Adoption Agency home page."""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add")
def display_add_pet_form():
    form = AddPetForm()
    return render_template("add_pet.html", form=form)

@app.route("/add", methods=["POST"])
def validate_pet_form():
    form = AddPetForm()
    if form.validate_on_submit():
        pet_inputs = form.data
        pet_inputs.pop("csrf_token", None)
        added_pet = Pet(**pet_inputs)
        db.session.add(added_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)