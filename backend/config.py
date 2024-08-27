import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DERIV5_PATH = os.getenv('DERIV5_PATH', 'C:\\Path\\To\\deriv5setup.exe')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    HOTMART_APP_ID = os.getenv('HOTMART_APP_ID')
    HOTMART_APP_SECRET = os.getenv('HOTMART_APP_SECRET')
