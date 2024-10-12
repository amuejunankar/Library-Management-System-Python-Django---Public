
import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g&ky9nvy1-hp6!08w)@=_@rug4-&(!%x%=&4bkivzwd7@e7o9u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',
    
    # Google AND Github Login
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware Social Login :
    "allauth.account.middleware.AccountMiddleware", 
    # Add this line in the middleware list
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# ----------------------------------------------------------------------------------
# ------------------------------------ Whitenoise ----------------------------------

# Efficient Serving: WhiteNoise allows your Django app to directly serve its own static files, removing the need for a separate web server. This speeds up the process by reducing the number of requests required to serve static content.

# Compression and Caching: WhiteNoise automatically compresses static files like CSS and JavaScript, making them smaller and faster to load. It also adds cache headers to these files, optimizing browser caching and reducing the need for repeated downloads.

# Seamless Integration: WhiteNoise seamlessly integrates with Django apps as middleware. It can handle static file requests alongside other middleware components, simplifying the setup and operation of your Django app.

# ----------------------------------------------------------------------------------

ROOT_URLCONF = 'library_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django Social Login
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'library_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# 

DATABASES = {
    'default': dj_database_url.parse("Paste DB Link Here")
}

# DATABASES = {
#     'default': dj_database_url.parse("Paste DB Link Here")
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


###  STATIC_URL: This is the URL to use when referring to static files.
###  STATICFILES_DIRS: This tells Django where to look for static files in development.
###  STATIC_ROOT: This is where Django will collect all static files for production.


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static", 
]

STATIC_ROOT = BASE_DIR / 'staticfiles' # for production
# Enable Whitenoise to serve static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==================================================================
# ============================  EMAIL =============================

# Email Backend Configuration (example for Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''  # Your Gmail email address
EMAIL_HOST_PASSWORD = ''  # Your Gmail password or app password


# ==================================================================
# ============================ GOOGLE LOGIN ========================

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_LOGIN_ON_GET = True   # Bypass to select account
 
SOCIALACCOUNT_PROVIDERS = { 
    'google': {
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'prompt': 'select_account',
        }
    },
    'github': {
        'APP': {
            'client_id': '',
            'secret': '',
        },
        'SCOPE': [
            'user',
            'repo',  # 
        ],
        'AUTH_PARAMS': {
            'redirect_uri': 'https://library-management-dbry.onrender.com/accounts/github/login/callback/',
        }
    }
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
