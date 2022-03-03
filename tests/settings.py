from django.conf import settings

SECRET_KEY = "tests"
DEBUG = True

# Supress unset TZ-Warning
USE_TZ = False

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {"debug": True},
    }
]
INSTALLED_APPS = settings.INSTALLED_APPS + [
    "wagtailaudioembed",
]
