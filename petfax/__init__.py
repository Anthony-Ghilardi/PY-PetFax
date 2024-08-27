from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Application factory
def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    # Initialize the database and migration engine
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # Index route
    @app.route('/')
    def index():
        return 'Hello, PetFax!'

    # Register the pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # Register the fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    # Return the app instance
    return app