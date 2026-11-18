import sqlite3

RATE_PER_CUBIC = 25

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
customer_id,
consumption
FROM meter_readings
""")

rows = cursor.fetchall()

bill_id = 1

for row in rows:

    customer_id = row[0]
    consumption = row[1]

    amount_due = (
        consumption
        * RATE_PER_CUBIC
    )

    cursor.execute("""
    INSERT INTO billings
    (
        bill_id,
        customer_id,
        billing_month,
        consumption,
        amount_due,
        due_date
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        bill_id,
        customer_id,
        "October 2026",
        consumption,
        amount_due,
        "2026-11-15"
    )
    )

    bill_id += 1

conn.commit()

conn.close()

print("Bills Generated Successfully")