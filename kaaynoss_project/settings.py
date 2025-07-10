from pathlib import Path
import os
import certifi  # ← pour sécuriser les connexions SSL/TLS avec Gmail

# === BASE DIR ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === TEMPLATES & STATIC FILES ===
TEMPLATES_DIR = BASE_DIR / 'siteweb' / 'templates'
STATICFILES_DIRS = [
    BASE_DIR / 'siteweb' / 'static'
]

# === SÉCURITÉ ===
SECRET_KEY = 'django-insecure--t$jy%!r$)&hzl!5i5r-2d2146hl$o$we0z51b3970j!@-lty9'
DEBUG = True
ALLOWED_HOSTS = []

# === APPLICATIONS INSTALLÉES ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'siteweb',  # Ton application personnalisée
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# === ROUTAGE ===
ROOT_URLCONF = 'kaaynoss_project.urls'

# === TEMPLATES ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

# === WSGI ===
WSGI_APPLICATION = 'kaaynoss_project.wsgi.application'

# === BASE DE DONNÉES ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === VALIDATEURS DE MOT DE PASSE ===
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

# === LOCALISATION ===
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === FICHIERS STATIQUES ===
STATIC_URL = '/static/'
STATICFILES_DIRS = STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / 'staticfiles'

# === PAR DÉFAUT ID AUTO ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === CONFIGURATION EMAIL POUR NOTIFICATIONS (ex: réservation) ===
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  # Ne pas activer les deux à la fois

# ✅ Ton adresse email (utilise une adresse Gmail)
EMAIL_HOST_USER = 'soracisse64@gmail.com'

# ✅ Mot de passe d'application (pas le mot de passe Gmail normal)
EMAIL_HOST_PASSWORD = 'vdxx dnco rqze jhdj'

#

# ✅ Email par défaut si "from_email" n'est pas précisé dans send_mail()
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kaaynoss_db',
        'USER': 'root',
        'PASSWORD': 'Senegal2022',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
