import dj_database_url
from microblog.settings.base  import *

# Allow local dev locally
# http://stackoverflow.com/questions/14795824/improperlyconfiguredsettings-databases-is-improperly-configured-error-when
DATABASES['default'] =  dj_database_url.config(default='postgres://vagrant:vagrant@localhost/microblog')

ALLOWED_HOSTS = ['localhost', 'glacial-forest-3650.herokuapp.com']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
