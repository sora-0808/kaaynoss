import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# === Définition de BASE_DIR ===
BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kaaynoss_project.settings')

# === Application Django ===
application = get_wsgi_application()

# === WhiteNoise pour servir les statiques ===
# Racine des fichiers statiques collectés
static_root = BASE_DIR / 'staticfiles'
application = WhiteNoise(application, root=str(static_root))
