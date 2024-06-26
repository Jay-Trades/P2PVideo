import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db():
    conn = sqlite3.connect('login.db', check_same_thread=False)
    try:
        yield conn
    finally:
        conn.close()
