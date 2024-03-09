"""
Database
https://docs.djangoproject.com/en/4.2/ref/settings/#database
"""
import os

from ..base import BASE_DIR

# DATABASES
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', BASE_DIR / 'db.sqlite3'),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
}

# DATABASE_ROUTERS
# https://docs.djangoproject.com/en/4.2/ref/settings/#database-routers

# DEFAULT_INDEX_TABLESPACE
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-index-tablespace

# DEFAULT_TABLESPACE
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-tablespace
