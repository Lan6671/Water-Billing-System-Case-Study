import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

readings = [
    (
        1,
        1,
        "2026-10-31",
        120,
        145,
        25
    ),
    (
        2,
        2,
        "2026-10-31",
        200,
        235,
        35
    ),
    (
        3,
        3,
        "2026-10-31",
        310,
        350,
        40
    )
]

cursor.executemany("""
INSERT INTO meter_readings
(
    reading_id,
    customer_id,
    reading_date,
    previous_reading,
    current_reading,
    consumption
)
VALUES (?, ?, ?, ?, ?, ?)
""", readings)

conn.commit()

conn.close()

print("Meter Reading Records Inserted Successfully")