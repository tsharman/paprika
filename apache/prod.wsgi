import os
import sys

path = '/paprika/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'paprika.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
