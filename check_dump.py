import os
import json
from django.core import serializers
from django.apps import apps

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.local')
import django
django.setup()

print("Создание дампа с поддержкой кириллицы...")

# Получаем все модели которые хотим сохранить
models_to_dump = []

# Попробуем получить модели из всех приложений
try:
    blog_post_model = apps.get_model('blogs', 'BlogPost')
    models_to_dump.extend(list(blog_post_model.objects.all()))
    print(f"✅ Найдены посты блога: {blog_post_model.objects.count()} шт")
except LookupError:
    print("⚠️ Модель BlogPost не найдена")

try:
    user_model = apps.get_model('auth', 'User')
    models_to_dump.extend(list(user_model.objects.all()))
    print(f"✅ Найдены пользователи: {user_model.objects.count()} шт")
except LookupError:
    print("⚠️ Модель User не найдена")

try:
    custom_user_model = apps.get_model('users', 'User')
    models_to_dump.extend(list(custom_user_model.objects.all()))
    print(f"✅ Найдены кастомные пользователи: {custom_user_model.objects.count()} шт")
except LookupError:
    print("⚠️ Кастомная модель User не найдена")

if not models_to_dump:
    print("❌ Не найдено ни одной модели для дампа!")
    exit()

# Создаем дамп
data = serializers.serialize("json",
    models_to_dump,
    use_natural_foreign_keys=True,
    use_natural_primary_keys=True,
    indent=2,
    ensure_ascii=False  # ← ВАЖНО! Сохраняем кириллицу как есть
)

# Сохраняем в файл
with open('datadump_cyrillic.json', 'w', encoding='utf-8') as f:
    f.write(data)

print(f"✅ Дамп создан: datadump_cyrillic.json")
print(f"📊 Размер файла: {os.path.getsize('datadump_cyrillic.json')} байт")
print(f"📝 Сохранено записей: {len(models_to_dump)}")