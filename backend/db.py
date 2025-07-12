# backend/db.py

import sqlite3
from datetime import datetime

DB_FILE = "database/skippio.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            section TEXT,
            vendor TEXT,
            item TEXT,
            wait_time REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_order(section, vendor, item, wait_time):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO orders (timestamp, section, vendor, item, wait_time) VALUES (?, ?, ?, ?, ?)",
                   (timestamp, section, vendor, item, wait_time))
    conn.commit()
    conn.close()

def get_all_orders():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
