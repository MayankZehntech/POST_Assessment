import boto3
import json
import os

def get_secret(secret_name):
    """
    Retrieve secret from AWS Secrets Manager.
    """
    # region_name = os.getenv('us-east-2', 'us-east-1')  # Default to 'us-east-1' if not set
    region_name = 'us-east-2' # Default to 'us-east-1' if not set
    
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager', region_name=region_name)
    
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        secret_dict = json.loads(secret)  # Parse the secret string into a dictionary
        return secret_dict
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise

