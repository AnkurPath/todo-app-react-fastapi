from dotenv import load_dotenv
import os

# Get the directory path of config.py
# Load the .env file
load_dotenv()

# Rest of your code...
API_VERSION = os.getenv("API_VERSION")
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
DEFAULT_PAGE_SIZE = os.getenv("DEFAULT_PAGE_SIZE")
