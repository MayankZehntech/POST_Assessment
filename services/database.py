from flask_sqlalchemy import SQLAlchemy
from services.secret_manager import get_secret
import os

# Initialize the SQLAlchemy object
db = SQLAlchemy()

def init_db(app):
    """
    Initialize the database with the Flask app using credentials from AWS Secrets Manager.
    """
    # secret_name = os.getenv('DB_SECRET_NAME', 'my-db-secret')  # Environment variable for secret name
    secret_name =  "aws/rds/sfsyncinstance-dev"  # Environment variable for secret name
    
    try:
        # Fetch credentials from AWS Secrets Manager
        secret = get_secret(secret_name)
        username = secret.get('username')
        password = secret.get('password')
        host = secret.get('host')
        database = secret.get('dbname')

        # Construct the database URI
        database_uri = f"postgresql://{username}:{password}@{host}/{database}"
        print('database URI:' ,database_uri)
        
        app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(app)
        print("Database connected successfully")

    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise



# from flask_sqlalchemy import SQLAlchemy
# import os
# # Initialize the SQLAlchemy object
# db = SQLAlchemy()

# def init_db(app):
#     """
#     Initialize the database with the Flask app.
#     """
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     if not os.getenv('DATABASE_URL'):
#         raise Exception("DATABASE_URL not set in environment.")

    
#     try:
#         db.init_app(app)
#         print("Database connected successfully")
#     except Exception as e:
#         print(f"Error connecting to the database: {e}")

