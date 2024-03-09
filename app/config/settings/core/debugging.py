"""
Debugging
https://docs.djangoproject.com/en/4.2/ref/settings/#debugging
"""
import os

# DEBUG
# https://docs.djangoproject.com/en/4.2/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DJANGO_DEBUG', default=0))

# DEBUG_PROPAGATE_EXCEPTIONS
# https://docs.djangoproject.com/en/4.2/ref/settings/#debug-propagate-exceptions
