import os.path


PROJ_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(PROJ_DIR, os.pardir))
DEBUG = True
ALLOWED_HOSTS = ['*', '127.0.0.1']
THUMBNAIL_DEBUG = True
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    # os.path.abspath(os.path.join(BASE_DIR, 'static')),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(STATIC_ROOT),
)
