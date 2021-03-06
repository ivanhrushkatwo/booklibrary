"""
Django settings for locallibrary project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4psf+*j*%ayk=#b2^6)&bjn&=e91+4=c7_k*q7^#o6u)kt=vyu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.110.0.10', ]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ------ Email settings ------------

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ivanhrushka.py@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
DEFAULT_FROM_EMAIL = 'ivanhrushka.py@gmail.com'

# ------ Email settings ------------

AUTH_USER_MODEL = "catalog.CustomUser"

LOGIN_URL = "users:auth_login"
LOGOUT_URL = "users:auth_logout"
REGISTRATION_OPEN = True
# Application definition

INSTALLED_APPS = [
    'django_admin_bootstrapped',    # before <- 'django.contrib.admin'
    'django.contrib.admin',

    'django.contrib.sites',
    'registration',                 # Before 'django.contrib.auth',
    'django.contrib.auth',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'social_django',                # Social auth
    'catalog',                      # 'catalog.apps.AppConfig'
    'django_ajax',
    'imagefit',
    'crispy_forms',
    'disqus',
    #'getpaid',
]


# -------------------- DISQUS  Settings  -------------------------------------------------------------------------------
DISQUS_API_KEY = 'uBMHChAOu9beNC5pt03SDiAZ0DqLFOvVCTmAEVccAzSl06AgPS3RHIVN8fZP6woq'
DISQUS_WEBSITE_SHORTNAME = 'marketbook'
# -------------------- End DISQUS Block --------------------------------------------------------------------------------


# ######################################################################################################################
# ---------------------------------------------- Social auth ----------------------------------------------------------#
# ######################################################################################################################

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_SANITIZE_REDIRECTS = True

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email',
}
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.8'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '1914622558772874'
SOCIAL_AUTH_FACEBOOK_SECRET = '550858429fedaaa31fee6c859aa2a9a8'

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '774304408997-cb9rqt7bb6rk8bmbt6n0tcuso74eu6kt.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'gET6Hoz7NOrvSJxVCoGWxIa5'

# ######################################################################################################################
# -------------------------------------------- End social auth --------------------------------------------------------#
# ######################################################################################################################


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'locallibrary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # social auth
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

                # my owd context processor - list with category
                'context_processors.custom_context_processor.category',

                # basket list
                'context_processors.custom_context_processor.basket_with_goods',

                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'locallibrary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bookmarket',
        'USER': 'admin_book',
        'PASSWORD': '2033',
        'HOST': 'localhost',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('uk', 'Ukrainian'),
    ('en', 'English'),)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "files/media")
MEDIA_URL = "/media/"

IMAGEFIT_ROOT = os.path.join(BASE_DIR, "files")
IMAGEFIT_EXT_TO_FORMAT = {'.jpg': 'jpeg', '.bmp': 'png'}
IMAGEFIT_PRESETS = {
    'thumbnail': {'width': 64, 'height': 64, 'crop': True},
}


ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1

