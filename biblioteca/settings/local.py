
from .base import *
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nuevaDB',  # dbbiblioteca
        'USER': 'postgres',
        'PASSWORD': '2241',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
