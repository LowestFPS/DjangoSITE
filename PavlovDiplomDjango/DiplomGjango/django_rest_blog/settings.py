import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-tg3^m@tpvy^f*jwf&p!f5wu56(cky5(=1ay&)bl!e(shs%(a_h"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "ckeditor",
    "ckeditor_uploader",
    "crispy_forms",
    "taggit",

    "main_app.apps.MainAppConfig",
    "blog_app.apps.BlogAppConfig",
    "feedback_app.apps.FeedbackAppConfig",
    "registration_app.apps.RegistrationAppConfig",
    "authorization_app.apps.AuthorizationAppConfig",
    "search_app.apps.SearchAppConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_rest_blog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "main_app/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_rest_blog.wsgi.application"



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]



LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Minsk"  # UTC +3

USE_I18N = True

USE_TZ = True



STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "main_app/static")
MEDIA_ROOT = os.path.join(BASE_DIR, "blog_app/static/blog_app/media")
MEDIA_URL = "/media/"



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

############################
## CKEDITOR CONFIGURATION ##
############################

CKEDITOR_JQUERY_URL = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        "allowedContent": True,
        "toolbar_Full": [
            [
                "Styles",
                "Format",
                "Bold",
                "Italic",
                "Underline",
                "Strike",
                "Subscript",
                "Superscript",
                "-",
                "RemoveFormat",
            ],
            ["Image", "Flash", "Table", "HorizontalRule"],
            ["TextColor", "BGColor"],
            ["Smiley", "sourcearea", "SpecialChar"],
            ["Link", "Unlink", "Anchor"],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "Blockquote",
                "CreateDiv",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
                "-",
                "BidiLtr",
                "BidiRtl",
                "Language",
            ],
            ["Source", "-", "Save", "NewPage", "Preview", "Print", "-", "Templates"],
            ["Cut", "Copy", "Paste", "PasteText", "PasteFromWord", "-", "Undo", "Redo"],
            ["Find", "Replace", "-", "SelectAll", "-", "Scayt"],
            ["Maximize", "ShowBlocks"],
        ],
    }
}
############################

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGOUT_REDIRECT_URL = "/"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'lowestfps@bk.ru'
EMAIL_HOST_PASSWORD = '333qtvaa9233'


TAGGIT_CASE_INSENSITIVE = True
