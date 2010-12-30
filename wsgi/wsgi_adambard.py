SITE_DIR = '/opt/apps/freelance-env/site'

import site
site.addsitedir(SITE_DIR)

import os
import sys

sys.path.append(SITE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'freelance.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


