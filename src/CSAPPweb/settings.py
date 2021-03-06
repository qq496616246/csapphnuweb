#coding=UTF-8
"""
Django settings for CSAPPweb project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.conf.global_settings import STATICFILES_DIRS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p1^n#5c47sur(t1xgv-7#9%#h0@pbrlho&!^r18r5d=0nv8nas'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#python manage.py runserver 0.0.0.0:8000
ALLOWED_HOSTS = ["10.0.0.80"]#"127.0.0.1:8000","192.168.1.110"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MainPage',
    'ClassSchedule',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # ����
SESSION_FILE_PATH = os.path.join(BASE_DIR , 'static/cache')       # �����ļ�·�������ΪNone����ʹ��tempfileģ���ȡһ����ʱ��ַtempfile.gettempdir()                                                            # �磺/var/folders/d3/j9tj0gz93dg06bmwxmhh6_xm0000gn/T
 
SESSION_COOKIE_NAME = "sessionid"                          # Session��cookie�������������ʱ��key������sessionid������ַ���
SESSION_COOKIE_PATH = "/"                                  # Session��cookie�����·��
SESSION_COOKIE_DOMAIN = None                                # Session��cookie���������
SESSION_COOKIE_SECURE = False                               # �Ƿ�Https����cookie
SESSION_COOKIE_HTTPONLY = True                              # �Ƿ�Session��cookieֻ֧��http����
SESSION_COOKIE_AGE = 1209600                                # Session��cookieʧЧ���ڣ�2�ܣ�
SESSION_EXPIRE_AT_BROWSER_CLOSE = True                     # �Ƿ�ر������ʹ��Session����
SESSION_SAVE_EVERY_REQUEST = False                          # �Ƿ�ÿ�����󶼱���Session��Ĭ���޸�֮��ű���
 
ROOT_URLCONF = 'CSAPPweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CSAPPweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DBNAME = 'csapp'
DATABASES = {
    'default': {
        'ENGINE' : "django.db.backends.dummy",
    }
}
from mongoengine import connect
connect('csapp')
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
      os.path.join(BASE_DIR , 'static'),
]
MEDIA_ROOT = os.path.join(BASE_DIR , "static/media/")
