# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError

from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

secret_name = "OpenAI_Category_Pirates"

# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager')

try:
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
except ClientError as e:
    # For a list of exceptions thrown, see
    # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    raise e

secret = json.loads(get_secret_value_response['SecretString'])
# set the environment variable
os.environ["OPENAI_API_KEY"] = secret['OPENAI_API_KEY']
    
    
