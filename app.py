import psycopg2
import os
import time

# Ждём пока БД проснётся
time.sleep(5)

for attempt in range(5):
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        break
    except psycopg2.OperationalError:
        print(f"Waiting for DB... attempt {attempt+1}/5")
        time.sleep(3)
else:
    raise Exception("Could not connect to DB after 5 attempts")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS final (
        id SERIAL PRIMARY KEY,
        name TEXT,
        ip TEXT,
        ips TEXT,
        created_at TIMESTAMP DEFAULT NOW()
    );
""")

cur.execute(
    "INSERT INTO final (name, ip, ips) VALUES (%s, %s, %s)",
    ("github-actions", "ci-cd", "works")
)

conn.commit()

cur.execute("SELECT * FROM final;")

for row in cur.fetchall():
    print(f"{row[0]} - Name: {row[1]}, ip: {row[2]}, ips: {row[3]}")

conn.close()
