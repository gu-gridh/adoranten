from .base import *

DEBUG = False 

SECRET_KEY = os.getenv('SECRET_KEY')

MEDIA_ROOT = os.getenv('MEDIA_ROOT')
MEDIA_URL = os.getenv('MEDIA_URL')
STATIC_ROOT = os.getenv('STATIC_ROOT')
STATIC_URL = os.getenv('STATIC_URL')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(",")

CORS_ALLOWED_ORIGINS = os.getenv("ORIGINS").split(",")

CORS_URLS_REGEX = r"^/api/v2/"

CSRF_TRUSTED_ORIGINS = os.getenv("ORIGINS").split(",")

try:
    from .local import *
except ImportError:
    pass
