from flask_sqlalchemy import SQLAlchemy
import os
# Initialize the SQLAlchemy object
db = SQLAlchemy()

def init_db(app):
    """
    Initialize the database with the Flask app.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not os.getenv('DATABASE_URL'):
        raise Exception("DATABASE_URL not set in environment.")

    
    try:
        db.init_app(app)
        print("Database connected successfully")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
