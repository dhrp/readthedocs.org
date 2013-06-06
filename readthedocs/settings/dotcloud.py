from .base import *  # noqa
import json

"""
Settings file meant to be run on dotCloud
"""

try:
    with open('/home/dotcloud/environment.json') as f:
        env = json.load(f)
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'rtfd',
                'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
                'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
                'HOST': env['DOTCLOUD_DB_SQL_HOST'],
                'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
                }
        }

except IOError:
    print 'Cannot load environment file (dotcloud). Maybe in local server ?'


DEBUG = False
TEMPLATE_DEBUG = False
CELERY_ALWAYS_EAGER = False

#MEDIA_URL = '//media.readthedocs.org/'
#STATIC_URL = '//media.readthedocs.org/static/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/dotcloud/data/media/'
STATIC_ROOT = '/home/dotcloud/volatile/static/'
STATIC_URL = '/static/'


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://odin:8983/solr',
        }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'PREFIX': 'docs',
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
        },
    }

SLUMBER_API_HOST = 'https://readthedocs.org'
WEBSOCKET_HOST = 'websocket.readthedocs.org:8088'

PRODUCTION_DOMAIN = 'readthedocs.org'
USE_SUBDOMAIN = True
NGINX_X_ACCEL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")


try:
    from local_settings import *  # noqa
except:
    pass
