from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_LOCAL_PASS'),
        'HOST': os.getenv('LOCAL_HOST'),
        'PORT': os.getenv('PORT'),
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]
CORS_URLS_REGEX = r"^/api/v2/"

try:
    from .local import *
except ImportError:
    pass
