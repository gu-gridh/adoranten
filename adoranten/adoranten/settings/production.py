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

CORS_URLS_REGEX = r"^/wagtail/api/v2/"

CSRF_TRUSTED_ORIGINS = os.getenv("ORIGINS").split(",")

WAGTAIL_HEADLESS_PREVIEW = {
    "CLIENT_URLS": {
        "default": os.getenv("MAINURL"),
    },  # defaults to an empty dict. You must at the very least define the default client URL.
    "SERVE_BASE_URL": None,  # can be used for HeadlessServeMixin
    "REDIRECT_ON_PREVIEW": False,  # set to True to redirect to the preview instead of using the Wagtail default mechanism
    "ENFORCE_TRAILING_SLASH": False,  # set to False in order to disable the trailing slash enforcement
}

try:
    from .local import *
except ImportError:
    pass
