import os
from .settings import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False