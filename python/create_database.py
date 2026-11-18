import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    address TEXT,
    meter_no TEXT,
    classification TEXT
)
""")

conn.commit()

conn.close()

print("Database Created Successfully")