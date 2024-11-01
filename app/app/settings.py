from pathlib import Path
from dotenv import load_dotenv
from decouple import config


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config("SECRET_KEY", default="test")


# DEBUG = config("DEBUG", cast=bool, default=True)
DEBUG = True


ALLOWED_HOSTS = ['*']

# ALLOWED_HOSTS = config(
#     "ALLOWED_HOSTS",
#     cast=lambda v: [s.strip() for s in v.split(",")],
#     default="*",
# )



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',
    'django_celery_beat',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'



# Postgres
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "appdatabase",
        "USER": "appuser",
        "PASSWORD": "appuser",
        "HOST": "postgres",
        "PORT": '5432',
    }
}




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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static and media files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT =  BASE_DIR / 'vol/shared/static/'
MEDIA_ROOT = BASE_DIR / 'vol/shared/media/'


STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# REDIS for cache
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',  # Redis database 1 for caching
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}



# Celery Configuration Options
CELERY_BROKER_URL = 'redis://redis:6379/0'  # Redis database 0 for Celery broker
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 300



# Beat Scheduler
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'


# CELERY Beat
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'core.tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
    'add-at-midnight': {
        'task': 'core.tasks.add',
        'schedule': crontab(minute=0, hour=0),
        'args': (16, 16)
    },
}


