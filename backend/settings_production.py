import os

import dj_database_url

from backend.settings_common import *  # noqa: F401,F403

DEBUG = True  # To turn off at some point

ALLOWED_HOSTS = [
    'foodie-map-backend.onrender.com',
    'foodie-map-frontend.onrender.com',
]

DATABASES = {
    "default": dj_database_url.parse(os.environ.get('DATABASE_URL')),
}

SECRET_KEY = os.environ.get('SECRET_KEY')
