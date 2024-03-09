"""
Static Files
https://docs.djangoproject.com/en/4.2/ref/settings/#static-files
"""
from .base import BASE_DIR

# STATIC_ROOT
# https://docs.djangoproject.com/en/4.2/ref/settings/#static-root
STATIC_ROOT = BASE_DIR / 'staticfiles'

# STATIC_URL
# https://docs.djangoproject.com/en/4.2/ref/settings/#static-url
STATIC_URL = 'static/'

# STATICFILES_DIRS
# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-dirs

# STATICFILES_STORAGE
# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-storage
# Deprecated since version 4.2

# STATICFILES_FINDERS
# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-finders
