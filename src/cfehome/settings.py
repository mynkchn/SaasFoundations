"""
Django settings for cfehome project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=config('EMAIL_HOST',cast=str,default='smtp.gmail.com')
EMAIL_PORT=config('EMAIL_PORT',cast=str,default='587')
EMAIL_HOST_USER=config('EMAIL_HOST_USER',cast=str,default=None)
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD',cast=str,default=None)
EMAIL_USE_SSL=config('EMAIL_USE_SSL',cast=bool,default=False)
EMAIL_USE_TLS=config('EMAIL_USE_TLS',cast=bool,default=False)

ADMIN_USER_NAME=config("ADMIN_USER_NAME", default="Admin user")
ADMIN_USER_EMAIL=config("ADMIN_USER_EMAIL", default=None)

MANAGERS=[]
ADMINS=[]
if all([ADMIN_USER_NAME, ADMIN_USER_EMAIL]):
    ADMINS +=[
        (f'{ADMIN_USER_NAME}', f'{ADMIN_USER_EMAIL}')
    ]
    MANAGERS=ADMINS



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG=str(os.environ.get('DEBUG')).lower()='true'
DEBUG = config('DJANGO_DEBUG',cast=bool)
#


ALLOWED_HOSTS = [
    '.railway.app' # https://saas.prod.railway.app
]
if DEBUG :
    ALLOWED_HOSTS+=['127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'visits.apps.VisitsConfig',
    # Create your own commands
    'commando.apps.CommandoConfig',
    # Authentication Check
    # 'auth.apps.AuthConfig',
    # Authentication using Third Party - remember sequence
    'allauth_ui',
    'allauth',
    'allauth.account',
    # requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    #  include the providers you want to enable:
    'allauth.socialaccount.providers.github',
    # UI For All Auth
    "widget_tweaks",
    "slippers",
]
ALLAUTH_UI_THEME = 'light'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
     # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]



# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

ROOT_URLCONF = 'cfehome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGIN_REDIRECT_URL='/'
ACCOUNT_AUTHENTICATION_METHOD='username_email'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION='mandatory'
# ACCOUNT_EMAIL_SUBJECT_PREFIX-"[CFE]"



# All Auth Module used for authentication using GitHub
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',

]

WSGI_APPLICATION = 'cfehome.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASE_URL=config('DATABASE_URL',default=None)
CONN_MAX_AGE=config('CONN_MAX_AGE',default=30,cast=int)
if DATABASE_URL is not None:
 import dj_database_url
 DATABASES = {
    'default': dj_database_url.config(
       default=DATABASE_URL,
       conn_health_checks=True,
       conn_max_age=CONN_MAX_AGE,
    )
        
    }


 CSRF_TRUSTED_ORGINS=[
    'https://saasfoundations-production-014d.up.railway.app/',
 ]
 CSRF_COOKIE_SECURE = True  # If using HTTPS, ensure this is True
 CSRF_COOKIE_HTTPONLY = True
 CSRF_COOKIE_SAMESITE = 'None'  # Required for cross-site cookies
 
   
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_BASE_DIR=BASE_DIR/'staticfiles'
STATICFILES_BASE_DIR.mkdir(exist_ok=True,parents=True)
STATICFILES_VENDOR_DIR=STATICFILES_BASE_DIR/'vendors'
STATICFILES_DIRS=[STATICFILES_BASE_DIR]
STATIC_ROOT = BASE_DIR / 'local-cdn'
#STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'

STORAGES={
   
   'staticfiles': {
      'BACKEND' : 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    }

}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

