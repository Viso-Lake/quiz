import os
from datetime import timedelta

from django.conf import settings

from config.api.rest_settings import *
from dotenv import load_dotenv

load_dotenv()

# настройки rest framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DATETIME_FORMAT": "%d.%m.%Y",
    "DATE_FORMAT": "%d.%m.%Y",
    "DATE_INPUT_FORMATS": [
        ("%d.%m.%Y"),
    ],
}


# настройки JWT токена
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": (
        timedelta(days=365) if settings.DEBUG else timedelta(minutes=15)
    ),
    "REFRESH_TOKEN_LIFETIME": (
        timedelta(days=365) if settings.DEBUG else timedelta(hours=1)
    ),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ROTATE_REFRESH_TOKENS": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": os.getenv("SECRET_KEY"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}
# конец настроек JWT токена
