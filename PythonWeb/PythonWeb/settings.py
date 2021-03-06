"""
Django settings for PythonWeb project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from captcha import *
import os
import sys
import platform

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qpbwqr#sy=l*q+s+kk(&03a*#a8elco55)+zw!wt4k#$!%hz3!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['143.110.147.190', '127.0.0.1', 'aione.studio', 'www.aione.studio']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.templatetags.template',
    'django_comments',
    'django.contrib.sites',
    # 'django.contrib.admin.apps.SimpleAdminConfig',
    'django.forms',
    'PythonWeb',
    'acfun',
    'bili',
    'login',
    'twitter',
    'youtube',
    'other',
    'captcha',
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PythonWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                "dealwithtime": "apps.templatetags.template",
                "isp2": "apps.templatetags.template",
                "makeurl": "apps.templatetags.template",
                "twpic": "apps.templatetags.template",
                "formatTimeFromYoutube": "apps.templatetags.template",
                "ToStr": "apps.templatetags.template",
            },
        },

    },
]

WSGI_APPLICATION = 'PythonWeb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if platform.system() == 'Windows':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'default.db'),
            # 'NAME': '/home/myspider/twitter/tweets.db',
        },
        'twitterdb': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'tweets.db'),
            # 'NAME': '/home/myspider/twitter/tweets.db',
        },
        'acfundb': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'acfun_data.db'),
            # 'NAME': '/home/myspider/acfun/acfun_data.db',
        },
        'bilidb': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'bili_data.db'),
            # 'NAME': '/home/myspider/bilidown/bili_data.db',
        },
        'youtube_db': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'data_youtube.db'),
            # 'NAME': '/home/myspider/youtube/data_youtube.db',
        },
        'logindb': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'login.db'),
        },
        'other_db': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db_other.db'),
        },

    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'default.db'),
            # 'NAME': '/home/myspider/twitter/tweets.db',
        },
        'twitterdb': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'tweets.db'),
            'NAME': '/home/myspider/twitter/tweets.db',
        },
        'acfundb': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'acfun_data.db'),
            'NAME': '/home/share/abd/acfun_data.db',
        },
        'bilidb': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'bili_data.db'),
            'NAME': '/home/myspider/bilidown/bili_data.db',
        },
        'youtube_db': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'data_youtube.db'),
            'NAME': '/home/myspider/youtube/data_youtube.db',
        },
        'logindb': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'login.db'),
        },
        'other_db': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db_other.db'),
        },

    }

DATABASE_ROUTERS = ['PythonWeb.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    # example:
    # 'app_name':'database_name',
    # 'core': 'default',
    # 'auth': 'default',
    # 'authtoken': 'default',
    'django.contrib.admin': 'default',
    'django.contrib.auth': 'default',
    'django.contrib.contenttypes': 'default',
    'django.contrib.sessions': 'default',
    'django.contrib.messages': 'default',
    'django.contrib.staticfiles': 'default',
    'PythonWeb': 'default',
    'twitter': 'twitterdb',
    'acfun': 'acfundb',
    'login': 'logindb',
    'bili': 'bilidb',
    'youtube': 'youtube_db',
    'captcha': 'default',
    'other': 'other_db',
    'django.contrib.sites': 'default',
    'django_comments': 'default',
    'django.contrib.sessions': 'default',
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Captcha Settings
CAPTCHA_LENGTH = 5

CAPTCHA_IMAGE_SIZE = (120, 25)

CAPTCHA_TIMEOUT = 1

CAPTCHA_TEXT_FIELD_TEMPLATE = os.path.join(BASE_DIR, './templates/other/field_template.html')

CAPTCHA_OUTPUT_FORMAT = u'%(image)s %(hidden_field)s %(text_field)s'
