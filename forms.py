from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf


# Springboard requirements: 
# • the species should be either “cat”, “dog”, or “porcupine”
# • the photo URL must be a URL (but it should still be able to be optional!)
# • the age should be between 0 and 30, if provided
class AddPetForm(FlaskForm):
    """Form for adding a pet to the adoption agency."""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[AnyOf("cat", "dog", "porcupine"), InputRequired()])
    photo_url = URLField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing a pet in the adoption agency."""

    photo_url = URLField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available for Adoption", Optional())
