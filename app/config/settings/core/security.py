"""
Security
https://docs.djangoproject.com/en/4.2/ref/settings/#security
"""
import os

# CSRF_COOKIE_DOMAIN
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-cookie-domain

# CSRF_COOKIE_MASKED
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-cookie-masked
# Deprecated since version 4.1

# CSRF_COOKIE_NAME
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-cookie-name

# CSRF_COOKIE_PATH
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-cookie-path

# CSRF_COOKIE_SAMESITE
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-cookie-samesite

# CSRF_COOKIE_SECURE
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-cookie-secure

# CSRF_FAILURE_VIEW
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-failure-view

# CSRF_HEADER_NAME
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-header-name

# CSRF_TRUSTED_ORIGINS
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = os.environ.get(
    'CSRF_TRUSTED_ORIGINS', default='http://localhost http://127.0.0.1'
).split(' ')

# CSRF_USE_SESSIONS
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-use-sessions

# SECRET_KEY
# https://docs.djangoproject.com/en/4.2/ref/settings/#secret-key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECRET_KEY_FALLBACKS
# https://docs.djangoproject.com/en/4.2/ref/settings/#secret-key-fallbacks

# X_FRAME_OPTIONS
# https://docs.djangoproject.com/en/4.2/ref/settings/#x-frame-options
