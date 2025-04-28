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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

try:
    from .local import *
except ImportError:
    pass
