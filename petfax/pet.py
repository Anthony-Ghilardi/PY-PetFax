from flask import Blueprint, render_template
import json

# Retrieve and open json file
pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

# Index route
@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

# Show route
@bp.route('/<int:pet_id>')
def show_pet(pet_id):
    pet = next((p for p in pets if p["pet_id"] == pet_id), None)
    if pet is None:
        return "Pet not found", 404
    return render_template('show.html', pet=pet)


# Create route
@bp.route('/pets/new')
def new_fact():
    return render_template('newfact.html')