import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS billings (
    bill_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    billing_month TEXT,
    consumption INTEGER,
    amount_due REAL,
    due_date TEXT
)
""")

conn.commit()

conn.close()

print("Billing Table Created Successfully")