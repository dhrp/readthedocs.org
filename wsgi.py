import os
import sys
#sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'readthedocs')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'readthedocs.settings.dotcloud'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

