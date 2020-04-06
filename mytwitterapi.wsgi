#mytwitterapi.wsgi
import sys
sys.path.insert(0, '/var/www/html/mytwitterapi')

from mytwitterapi import app as application
