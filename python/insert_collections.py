import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

collections = [
    (
        1,
        1,
        "OR-1001",
        "2026-11-05",
        625
    ),
    (
        2,
        2,
        "OR-1002",
        "2026-11-05",
        875
    )
]

cursor.executemany("""
INSERT INTO collections
(
    collection_id,
    bill_id,
    or_no,
    payment_date,
    amount_paid
)
VALUES (?, ?, ?, ?, ?)
""", collections)

conn.commit()

conn.close()

print("Collections Posted Successfully")
