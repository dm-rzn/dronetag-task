from pathlib import Path
from environs import Env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
EXTERNAL_STORAGE = 'external_storage'


#######################################################################################################################
#
#
#                                                        Shell
#
#
########################################################################################################################
SHELL_PLUS = 'ipython'
IPYTHON_ARGUMENTS = [
    '--ext', 'autoreload',
]

#######################################################################################################################
#
#
#                                               Application definition
#
#
########################################################################################################################
ROOT_URLCONF = 'flight_analysis.urls'


#######################################################################################################################
#
#
#                                               Environment variables
#
#
########################################################################################################################
env = Env()
env.read_env()

DEBUG = env.bool('DJANGO_DEBUG')
SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')


#######################################################################################################################
#
#
#                                                   Databases
#
#
########################################################################################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_NAME'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env.int('POSTGRES_PORT'),
        'OPTIONS': {
            'client_encoding': 'UTF8',
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#######################################################################################################################
#
#
#                                              Password validation
#
#
########################################################################################################################
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

AUTH_USER_MODEL = 'users.User'


#######################################################################################################################
#
#
#                                               Internationalization
#
#
########################################################################################################################
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

USE_THOUSAND_SEPARATOR = True


#######################################################################################################################
#
#
#                                                   Statics
#
#
########################################################################################################################
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / EXTERNAL_STORAGE / 'media'
STATIC_ROOT = BASE_DIR / EXTERNAL_STORAGE / 'static'

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

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
            ],
        },
    },
]


#######################################################################################################################
#
#
#                                                 Middleware
#
#
########################################################################################################################
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


#######################################################################################################################
#
#
#                                                Django Apps
#
#
########################################################################################################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_extensions',
    'import_export',
    'flight_analysis',
    # ----------------------------
    'users',
    'common',
    'telemetry',
    # ----------------------------
]

#######################################################################################################################
#
#
#                                                   Caches
#
#
#######################################################################################################################
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
    },
}


#######################################################################################################################
#
#
#                                                   Files
#
#
#######################################################################################################################
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]


#######################################################################################################################
#
#
#                                                   Logging
#
#
########################################################################################################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s]: %(message)s'
        }
    },
    'handlers': {
        'django': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / EXTERNAL_STORAGE / 'logs' / 'django.log',
            'maxBytes': 1024 * 1024 * 10,    # 10MB
            'backupCount': 10,
            'formatter': 'standard'
        },
        'console': {
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django'],
            'level': 'INFO',
            'propagate': True
        },
    }
}


#######################################################################################################################
#
#
#                                                   Import export
#
#
#######################################################################################################################
from import_export.formats.base_formats import CSV  # noqa: E402

IMPORT_EXPORT_FORMATS = [CSV]
