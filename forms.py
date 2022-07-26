from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, TextAreaField, BooleanField
from wtforms.validators import (
    InputRequired,
    Optional,
    URL,
    NumberRange,
    AnyOf,
)


# Springboard requirements:
# • the species should be either “cat”, “dog”, or “porcupine”
# • the photo URL must be a URL (but it should still be able to be optional!)
# • the age should be between 0 and 30, if provided
class AddPetForm(FlaskForm):
    """Form for adding a pet to the adoption agency."""

    @classmethod
    def title_string(cls, str=""):
        """Returns a title-cased version of a truthy string."""
        if str:
            return str.title()
        else:
            return str

    name = StringField(
        "Name",
        validators=[InputRequired(message="The pet's name is required.")],
    )
    species = StringField(
        "Species",
        validators=[
            AnyOf(
                ["Cat", "Dog", "Porcupine"],
                message="The species must be a cat, dog, or porcupine.",
            ),
            InputRequired(message="The pet's species is required."),
        ],
        filters=[lambda str: AddPetForm.title_string(str)],
    )
    photo_url = URLField(
        "Photo URL",
        validators=[Optional(), URL(message="That photo link was not a valid URL.")],
        filters=[lambda url: url or None],
    )
    age = IntegerField(
        "Pet Age",
        validators=[
            Optional(),
            NumberRange(
                min=0, max=30, message="The valid age range is 0 - 30, inclusive."
            ),
        ],
    )
    notes = TextAreaField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing a pet in the adoption agency."""

    available = BooleanField("Available", validators=[Optional()])
    photo_url = URLField(
        "Photo URL",
        validators=[Optional(), URL(message="That photo link was not a valid URL.")],
    )
    notes = TextAreaField("Notes", validators=[Optional()])
