import os
from django.core.wsgi import get_wsgi_application

_ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_demo.settings")
application = get_wsgi_application()
