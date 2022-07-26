from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to the Adoption database"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Class representing a pet from the Adoption Agency"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url= db.Column(db.Text, default="static/assets/paw-heart.png")
    age = db.Column(db.Integer)
    notes= db.Column(db.Text, nullable=False)
    available= db.Column(db.Boolean, nullable=False, default=True)

    @property
    def summary(self):
        """Returns a brief summary of the pet"""
        return f"{self.name}, the {self.species}"
    
    def avail_details(self):
        """Returns a string describing this pet's adoption status."""
        if self.available:
            return f"{self.name} is available for adoption!"
        else:
            return f"{self.name} is not available for adoption."