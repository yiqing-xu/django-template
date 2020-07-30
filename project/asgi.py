# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 18:49
# @Author  : xuyiqing
# @File    : asgi.py
"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.dev_settings")
django.setup()
application = get_default_application()
