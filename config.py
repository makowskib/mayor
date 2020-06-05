import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'secret'
CSRF_SECRET = 'secret'

