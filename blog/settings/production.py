from .base import *

# DEBUG = False
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'arikmetiz_blog',
#         'USER': 'postgres',
#         'PASSWORD': 'mysecretpassword',
#         'HOST': '172.18.0.2',
#         'PORT': '5432',
#     }
# }



DEBUG = False

# Разрешаем локальные хосты для тестирования
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'simba72.ru']

# Настройки PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'arikmetiz_blog',           # имя базы которую создал в pgAdmin
        'USER': 'postgres',                 # пользователь
        'PASSWORD': 'mysecretpassword',     # пароль который указывал при создании контейнера
        'HOST': '172.18.0.2',              # IP который сработал в pgAdmin
        'PORT': '5432',                     # порт
    }
}

# Для безопасности (позже настроим через переменные окружения)
SECRET_KEY = 'your-secret-key-here'  # временно, потом заменим