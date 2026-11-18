import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS meter_readings (
    reading_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    reading_date TEXT,
    previous_reading INTEGER,
    current_reading INTEGER,
    consumption INTEGER
)
""")

conn.commit()

conn.close()

print("Meter Reading Table Created Successfully")