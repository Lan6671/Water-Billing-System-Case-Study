import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

customers = [
    (
        1,
        "Juan Dela Cruz",
        "Talavera",
        "MTR-001",
        "Residential"
    ),
    (
        2,
        "Maria Santos",
        "Talavera",
        "MTR-002",
        "Residential"
    ),
    (
        3,
        "Pedro Reyes",
        "Talavera",
        "MTR-003",
        "Commercial"
    )
]

cursor.executemany("""

INSERT INTO customers
(
    customer_id,
    customer_name,
    address,
    meter_no,
    classification
)

VALUES (?, ?, ?, ?, ?)

""", customers)

conn.commit()

conn.close()

print("Customer records inserted successfully.")