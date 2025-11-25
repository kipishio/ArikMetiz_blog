import os
import django

# Указываем Django, какой settings использовать
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings.local")  # твой локальный settings
django.setup()

from django.core.management import call_command

# Теперь можно дампить данные
with open('data.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', '--natural-primary', '--natural-foreign', '--indent', '2', stdout=f)
