"""
File uploads
https://docs.djangoproject.com/en/4.2/ref/settings/#file-uploads
"""
from ..base import BASE_DIR

# DEFAULT_FILE_STORAGE
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-file-storage
# Deprecated since version 4.2

# FILE_UPLOAD_HANDLERS
# https://docs.djangoproject.com/en/4.2/ref/settings/#file-upload-handlers

# FILE_UPLOAD_MAX_MEMORY_SIZE
# https://docs.djangoproject.com/en/4.2/ref/settings/#file-upload-max-memory-size

# FILE_UPLOAD_PERMISSIONS
# https://docs.djangoproject.com/en/4.2/ref/settings/#file-upload-permissions

# FILE_UPLOAD_TEMP_DIR
# https://docs.djangoproject.com/en/4.2/ref/settings/#file-upload-temp-dir

# MEDIA_ROOT
# https://docs.djangoproject.com/en/4.2/ref/settings/#media-root
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# MEDIA_URL
# https://docs.djangoproject.com/en/4.2/ref/settings/#media-url
MEDIA_URL = 'media/'

# STORAGES
# https://docs.djangoproject.com/en/4.2/ref/settings/#storages
