from flask import Flask

# App Factory
def create_app():
    app = Flask(__name__)
    
    # Register pet blueprint
    from.import pet
    app.register_blueprint(pet.bp)
    
    # Index Route
    @app.route('/')
    def hello():
        return
    
    # Show route
    @app.route('/pet/<int:pet_id>')
    def show_pet(pet_id):
        return f'Pet {pet_id}'

    # Create route not needed as already handled by the blueprint
    
    return app