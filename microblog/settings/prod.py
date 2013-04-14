import dj_database_url
from microblog.settings.base  import *

DATABASES['default'] =  dj_database_url.config()
ALLOWED_HOSTS = ['glacial-forest-3650.herokuapp.com']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
