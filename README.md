# Adopt
An example of a pet-adoption agency that uses a server database to record pet information.

## Usage
Pets on the site are stored in a corresponding table in the database, recording their name, species, age, photo url, adoption availability, and any notes on the pet.

The pets are displayed on the home page, and their detailed pages will display aditional information about them.
The details page also contains an edit form to alter the availability status, photo url, or pet notes.

Information is stored in a server-side database using PostgreSQL, accessed via Flask-Sqlalchemy. Forms and additional form validation is performed using WTForms, accessed via Flask-WTF.

The app is hosted on Heroku and is available at https://acollino-adopt.herokuapp.com.

## Previews
<img src="https://user-images.githubusercontent.com/8853721/181092359-c2090b9a-94d7-4fca-b8cf-17cd1d8a541c.png" alt="Adopt home page" style="width: 700px">

<img src="https://user-images.githubusercontent.com/8853721/181092555-c9b3e4ae-787e-458c-a5b2-994f8ecc8999.png" alt="Adopt pet-details page" style="width: 500px">

<img src="https://user-images.githubusercontent.com/8853721/181092663-7f54fac2-5c0b-4ad6-94ca-9a34a9696773.png" alt="Adopt page for submitting a new pet" style="width: 500px">

<img src="https://user-images.githubusercontent.com/8853721/181092974-1724499a-20ae-49e5-ab96-2cb5eca43e7f.png" alt="Adopt pet-details page, displaying the red-invalid input warning for the photo URL" style="width: 500px">


## Attributions
**Navigation Bar Font:** [Chewy, on Google Fonts](https://fonts.google.com/specimen/Chewy)

**Dog and Cat Icon:** [Created by Becris - Flaticon](https://www.flaticon.com/free-icons/cat)

**Paw-Heart Default Photo:** [Created by Freepik - Flaticon](https://www.flaticon.com/free-icons/dog)

**Pet Images, from Pixabay:** [Peanut](https://pixabay.com/photos/cat-tabby-surprised-cat-s-eyes-618470/), [Mr. Sootpaws](https://pixabay.com/photos/maine-coon-cat-cat-s-eyes-black-cat-694730/), [Einstein](https://pixabay.com/photos/corgi-dog-pet-canine-rain-animal-4415649/), [Penelope](https://pixabay.com/photos/nature-animal-porcupine-mammal-3588682/), [Lola](https://pixabay.com/photos/animal-company-dog-animals-animal-3047244/)
