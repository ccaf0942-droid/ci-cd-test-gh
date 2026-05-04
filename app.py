import psycopg2
import time
import os

time.sleep(3)

conn = psycopg2.connect(

    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")

)

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
    ("sex", "even", "67")
)

conn.commit()

cur.execute("SELECT * FROM final;")

for row in cur.fetchall():
    print(f"{row[0]} - Name: {row[1]}, ip: {row[2]}, ips: {row[3]}")

conn.close()