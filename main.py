from flask import Flask
from services.database import init_db
from routes.routes import routes
from dotenv import load_dotenv
from services.database import db

def create_app():
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv()
   
    # Create database
    init_db(app)

     # Automatically create the tables if they don't exist
    with app.app_context():
        db.create_all()  # This will create tables based on your models


    # Register routes
    app.register_blueprint(routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
