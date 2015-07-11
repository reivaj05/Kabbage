from .base import *  # noqa
from kabbage.keys import development

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = development.SECRET_KEY
TWITTER_API_KEY = 'Nf2PtCrCV3BP7OCoBrSQtTTMv'
TWITTER_ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAG08ggAAAAAAInQC6sn76lvMoPqlp%2BB0zoMfIbI%3Dzur7aPza2FOdG6X3jh07CX6dGbLwSXqI4BTOHRDiwV1U2xgxtz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vagrant',
        'USER': 'vagrant',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# This IP addresses ensure debug toolbar shows development environment
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')
