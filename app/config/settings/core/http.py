"""
HTTP
https://docs.djangoproject.com/en/4.2/ref/settings/#http
"""
import os

# ALLOWED_HOSTS
# https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', default='').split(' ')

# DATA_UPLOAD_MAX_MEMORY_SIZE
# https://docs.djangoproject.com/en/4.2/ref/settings/#data-upload-max-memory-size

# DATA_UPLOAD_MAX_NUMBER_FIELDS
# https://docs.djangoproject.com/en/4.2/ref/settings/#data-upload-max-number-fields

# DATA_UPLOAD_MAX_NUMBER_FILES
# https://docs.djangoproject.com/en/4.2/ref/settings/#data-upload-max-number-files

# DEFAULT_CHARSET
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-charset

# DISALLOWED_USER_AGENTS
# https://docs.djangoproject.com/en/4.2/ref/settings/#disallowed-user-agents

# FORCE_SCRIPT_NAME
# https://docs.djangoproject.com/en/4.2/ref/settings/#force-script-name

# INTERNAL_IPS
# https://docs.djangoproject.com/en/4.2/ref/settings/#internal-ips

# MIDDLEWARE
# https://docs.djangoproject.com/en/4.2/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# SECURE_CONTENT_TYPE_NOSNIFF
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-content-type-nosniff

# SECURE_CROSS_ORIGIN_OPENER_POLICY
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-cross-origin-opener-policy

# SECURE_HSTS_INCLUDE_SUBDOMAINS
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-hsts-include-subdomains

# SECURE_HSTS_PRELOAD
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-hsts-preload

# SECURE_HSTS_SECONDS
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-hsts-seconds

# SECURE_PROXY_SSL_HEADER
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-proxy-ssl-header

# SECURE_REDIRECT_EXEMPT
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-redirect-exempt

# SECURE_REFERRER_POLICY
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-referrer-policy

# SECURE_SSL_HOST
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-ssl-host

# SECURE_SSL_REDIRECT
# https://docs.djangoproject.com/en/4.2/ref/settings/#secure-ssl-redirect

# SIGNING_BACKEND
# https://docs.djangoproject.com/en/4.2/ref/settings/#signing-backend

# USE_X_FORWARDED_HOST
# https://docs.djangoproject.com/en/4.2/ref/settings/#use-x-forwarded-host

# USE_X_FORWARDED_PORT
# https://docs.djangoproject.com/en/4.2/ref/settings/#use-x-forwarded-port

# WSGI_APPLICATION
# https://docs.djangoproject.com/en/4.2/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'
