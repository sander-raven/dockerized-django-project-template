"""
Auth
https://docs.djangoproject.com/en/4.2/ref/settings/#auth
"""

# AUTHENTICATION_BACKENDS
# https://docs.djangoproject.com/en/4.2/ref/settings/#authentication-backends

# AUTH_PASSWORD_VALIDATORS
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# AUTH_USER_MODEL
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-user-model

# LOGIN_REDIRECT_URL
# https://docs.djangoproject.com/en/4.2/ref/settings/#login-redirect-url

# LOGIN_URL
# https://docs.djangoproject.com/en/4.2/ref/settings/#login-url

# LOGOUT_REDIRECT_URL
# https://docs.djangoproject.com/en/4.2/ref/settings/#logout-redirect-url

# PASSWORD_RESET_TIMEOUT
# https://docs.djangoproject.com/en/4.2/ref/settings/#password-reset-timeout

# PASSWORD_HASHERS
# https://docs.djangoproject.com/en/4.2/ref/settings/#password-hashers
