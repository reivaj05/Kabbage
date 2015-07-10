#!/usr/bin/env python
import os
import sys

name_project = 'kabbage'
if __name__ == "__main__":

    if os.path.exists(name_project+'/keys/production.py'):
        DJANGO_SETTINGS_MODULE = name_project+'.settings.production'
    else:
        DJANGO_SETTINGS_MODULE = name_project+'.settings.development'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
