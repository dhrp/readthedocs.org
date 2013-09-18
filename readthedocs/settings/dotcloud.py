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
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'rtfd',
                'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
                'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
                'HOST': env['DOTCLOUD_DB_SQL_HOST'],
                'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
                }
        }


        REDIS = {
            'host': env['DOTCLOUD_CACHE_REDIS_HOST'],
            'port': int(env['DOTCLOUD_CACHE_REDIS_PORT']),
            'db': 0,
#            'password': env['DOTCLOUD_CACHE_REDIS_LOGIN'],
            'password': env['DOTCLOUD_CACHE_REDIS_PASSWORD']
        }

        BROKER_URL = env['DOTCLOUD_CACHE_REDIS_URL']

        SLUMBER_USERNAME = 'admin'
        SLUMBER_PASSWORD = env['SLUMBER_PASS']
        SLUMBER_API_HOST = 'https://{}'.format(env['DOTCLOUD_WWW_HTTP_HOST'])

        # production domain is required, introduced with django 1.4 for security
        PRODUCTION_DOMAIN = env['DOTCLOUD_WWW_HTTP_HOST']
        SESSION_COOKIE_DOMAIN = env['DOTCLOUD_WWW_HTTP_HOST']

except IOError:
    print 'Cannot load environment file (dotcloud). Maybe in local server ?'

from unipath import Path
PROJECT_ROOT = Path(__file__).ancestor(3)


DEBUG = False
TEMPLATE_DEBUG = DEBUG
CELERY_ALWAYS_EAGER = False

#MEDIA_URL = '//media.readthedocs.org/'
#STATIC_URL = '//media.readthedocs.org/static/'
#ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
#SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_ENGINE = "django.contrib.sessions.backends.db"



MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/dotcloud/current/media'
STATIC_ROOT = '/home/dotcloud/volatile/static/'
STATIC_URL = '/static/'

# this value is not used as such, just the fact that it exists
#MULTIPLE_APP_SERVERS = ["docs-docker.dotcloud.com", ]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        },
    }

#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://odin:8983/solr',
#        }
#}
#
#CACHES = {
#    'default': {
#        'BACKEND': 'redis_cache.RedisCache',
#        'LOCATION': 'localhost:6379',
#        'PREFIX': 'docs',
#        'OPTIONS': {
#            'DB': 1,
#            'PARSER_CLASS': 'redis.connection.HiredisParser'
#        },
#        },
#    }

#WEBSOCKET_HOST = 'websocket.readthedocs.org:8088'
#

#USE_SUBDOMAIN = True
#NGINX_X_ACCEL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")


try:
    from local_settings import *  # noqa
except:
    pass
