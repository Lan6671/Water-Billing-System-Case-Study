import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS collections (
    collection_id INTEGER PRIMARY KEY,
    bill_id INTEGER,
    or_no TEXT,
    payment_date TEXT,
    amount_paid REAL
)
""")

conn.commit()

conn.close()

print("Collections Table Created Successfully")