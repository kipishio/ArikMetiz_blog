import psycopg
import sys

print("Python version:", sys.version)
print("psycopg version:", psycopg.__version__)

try:
    print("Пробую подключиться через psycopg3...")

    conn = psycopg.connect(
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        dbname="postgres"
    )

    print("✅ УСПЕХ! Подключение установлено")

    cur = conn.cursor()
    cur.execute("SELECT version()")
    print("Версия PostgreSQL:", cur.fetchone()[0])

    # Проверим базы
    cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false")
    dbs = cur.fetchall()
    print("Базы данных:", [db[0] for db in dbs])

    conn.close()

except Exception as e:
    print("❌ Ошибка:", str(e))
    print("Тип ошибки:", type(e).__name__)