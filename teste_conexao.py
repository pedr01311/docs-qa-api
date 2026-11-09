import psycopg 
import os
from dotenv import load_dotenv

load_dotenv()

with psycopg.connect(f"dbname={os.environ['DB_NAME']} user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']} host={os.environ['DB_HOST']} port={os.environ['DB_PORT']}") as conn:
    with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE IF NOT EXISTS test (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)


        conn.commit()

        cur.execute("INSERT INTO test (id, name) VALUES (2, 'admin') ON CONFLICT (id) DO NOTHING;")
        conn.commit()

        cur.execute("SELECT * FROM test")
        for i in cur:
            print(i)

        conn.commit()