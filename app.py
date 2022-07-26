from flask import Flask, request, render_template, redirect
from models import Pet, db, connect_db
from forms import AddPetForm, EditPetForm
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
    seed_pets = [Pet(name="Peanut", species="cat", photo_url="https://cdn.pixabay.com/photo/2015/01/31/12/36/cat-618470_960_720.jpg", age=1, notes="A bit skittish, but does well with other cats. Looking to be adopted into a multi-cat household!"),
                  Pet(name="Mr. Sootpaws", species="cat", photo_url="https://cdn.pixabay.com/photo/2015/03/27/13/16/maine-coon-694730_960_720.jpg", age=4, notes="His favorite game is hunting socks...while you are wearing them!"),
                  Pet(name="Einstein", species="dog", photo_url="https://cdn.pixabay.com/photo/2019/08/19/07/45/corgi-4415649_960_720.jpg", age=4, notes="Despite his name, Einstein isn't all that bright. But this doofus is still full of love and would love to join your family!"),
                  Pet(name="Penelope", species="porcupine", photo_url="https://cdn.pixabay.com/photo/2018/08/06/23/32/nature-3588682_960_720.jpg", notes="Careful, she's a hugger! Awaiting transfer to a local zoo; porcupines do not do well as house pets.", available=False), 
                  Pet(name="Lola", species="dog", photo_url="https://cdn.pixabay.com/photo/2017/12/29/10/47/animal-company-3047244_960_720.jpg", age=3, notes="Lola has loads of energy, loves to run, and has a knack for escaping enclosures if she's bored. Looking for an active family!")]
    db.session.add_all(seed_pets)
    db.session.commit()

@app.route("/")
def display_home_page():
    """Displays the Adoption Agency home page."""
    pets = Pet.query.order_by(Pet.id).all()
    return render_template("home.html", pets=pets)

@app.route("/add")
def display_add_pet_form():
    """Display the form to add a pet to the agency."""
    form = AddPetForm()
    return render_template("add_pet.html", form=form)

@app.route("/add", methods=["POST"])
def add_pet():
    """Validates the submitted pet and adds it to the database if successful.
        Otherwise, returns to the add_pet page with error messages visible."""
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

@app.route("/<int:pet_id>")
def display_pet_details(pet_id):
    """Display details about a pet."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    form.photo_url.data = ""
    return render_template("pet_details.html", form=form, pet=pet)

@app.route("/<int:pet_id>", methods=["POST"])
def edit_pet(pet_id):
    """Validates the edited pet details, updates the listing in the database if successful.
        Otherwise, returns to the pet_details page with error messages visible."""
    form = EditPetForm()
    pet = Pet.query.get_or_404(pet_id)
    if form.validate_on_submit():
        if not form.photo_url.data:
            form.photo_url.data = pet.photo_url
        form.populate_obj(pet)
        db.session.commit()
        return redirect("/")
    else:
        form.available = pet.available
        return render_template("pet_details.html", form=form, pet=pet)
    