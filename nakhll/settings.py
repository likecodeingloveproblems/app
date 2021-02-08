"""
Django settings for nakhll project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGIN = '/profile/dashboard/'
LOGIN_REDIRECT_URL = '/profile/dashboard/'
LOGOUT_REDIRECT_URL = '/'
REDIRECT_FIELD_NAME = 'next'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ") 

COMPRESS_ENABLED = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'sms',
    'my_auth',
    'tinymce',
    'django_jalali',
    'admin_reorder',
    'nakhll_market',
    'Payment',
    'Ticketing',
    'restapi',
    'oauth2_provider',
    'rest_framework',
    'rest_framework.authtoken',
    'imagekit',
    'compressor',
    'mathfilters',
    'instagram',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'middlewares.track_url_history.TrackUrlHistory',
]

ADMIN_REORDER = (
    {'app': 'nakhll_market','models':(
        'nakhll_market.Pages',
        'nakhll_market.Profile',
        'nakhll_market.Market',
        'nakhll_market.SubMarket',
        'nakhll_market.Shop',
        'nakhll_market.Product',
        'nakhll_market.ProductBanner',
        'nakhll_market.Category',
        'nakhll_market.Tag',
        'nakhll_market.Attribute',
        'nakhll_market.AttrPrice',
        'nakhll_market.Comment',
        'nakhll_market.Review',
        'nakhll_market.Message',
        'nakhll_market.Survey',
        'nakhll_market.Slider',
        'nakhll_market.Option_Meta',
        'nakhll_market.Alert',
        'nakhll_market.Newsletters',
    )},

    {'app': 'Payment', 'label': 'بخش مالی','models':(
        'Payment.Wallet',
        'Payment.Factor',
        'Payment.PostBarCode',
        'Payment.ManegerFactor',
        'Payment.Transaction',
        'Payment.Coupon',
        'Payment.Campaign',
        'Payment.Installment',
        'Payment.Invitation',
        'Payment.PecOrder',
        'Payment.PecTransaction',
        'Payment.PecConfirmation',        
        'Payment.PecReverse',        
    )},
    
    {'app': 'Ticketing', 'label': 'بخش پشتیبانی و گزارشات','models':(
        'Ticketing.Ticketing',
    )},

    {'app': 'auth','label':'کاربران و دسترسی ها'},
    
    {'app': 'sites','label':'دسترسی SiteMap'},
    
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

ROOT_URLCONF = 'nakhll.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates/')],
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


WSGI_APPLICATION = 'nakhll.wsgi.application'
IMAGEKIT_CACHEFILE_DIR = 'media/CACHE/images'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


PERSISTENT_STORAGE = "/mnt/shared-volume"

DATABASES = {
    # "mysql": {
    #     "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.mysql"),
    #     "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
    #     "USER": os.environ.get("SQL_USER", "user"),
    #     "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
    #     "HOST": os.environ.get("SQL_HOST", "localhost"),
    #     "PORT": os.environ.get("SQL_PORT", "3306"),
    #     'OPTIONS': {
    #         # Tell MySQLdb to connect with 'utf8mb4' character set
    #         'charset': 'utf8mb4',
    #     },
    #     'CONN_MAX_AGE': None,
    # },
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'nakhlldb'),
        'USER': os.environ.get('POSTGRES_USER', 'nakhll'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '12345'),
        'HOST':'postgres',
        'PORT':'5432',
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '')
MEDIA_URL = '/'

SESSION_COOKIE_AGE = 216000

CART_SESSION_ID = 'cart'

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
    'OAUTH_BACKEND_CLASS' : 'oauth2_provider.oauth2_backends.JSONOAuthLibCore',
    'ACCESS_TOKEN_EXPIRE_SECONDS': 86400,
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

SITE_ID = os.environ.get('SITE_ID',2)

# admin users that detail trace back of unhandelled exception are sent to them.
ADMINS = [tuple(os.environ.get('ADMINS').split())]
SERVER_EMAIL = os.environ.get('EMAIL_HOST_USER')

# setup email configurations
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS'))
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)

# setup sentry
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DNS"),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    environment=os.environ.get("SENTRY_ENVIRONMENT", "production"),
    send_default_pii=True,
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

KAVENEGAR_KEY = os.environ.get('KAVENEGAR_KEY')

SESSION_SAVE_EVERY_REQUEST: bool=True
