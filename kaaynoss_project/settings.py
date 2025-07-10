from pathlib import Path
import os

# === BASE DIR ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === TEMPLATES & STATIC FILES ===
TEMPLATES_DIR = BASE_DIR / 'siteweb' / 'templates'
STATICFILES_DIRS = [BASE_DIR / 'siteweb' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'


# === SÉCURITÉ ===
SECRET_KEY = 'django-insecure--t$jy%!r$)&hzl!5i5r-2d2146hl$o$we0z51b3970j!@-lty9'
DEBUG = False  # 🔒 IMPORTANT pour la production

ALLOWED_HOSTS = ['kaaynoss01.onrender.com', 'localhost', '127.0.0.1']
 # ✅ Remplace par ton nom d’utilisateur

# === APPLICATIONS INSTALLÉES ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'siteweb',
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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'soramalick',            # 🔁 Remplace par le nom de ta base sur PythonAnywhere
        'USER': 'soramalick',        # 🔁 Remplace par ton nom utilisateur PythonAnywhere
        'PASSWORD': 'Senegal2022',       # 🔁 Mot de passe MySQL
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# === VALIDATEURS DE MOT DE PASSE ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
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

# === ID AUTO PAR DÉFAUT ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
