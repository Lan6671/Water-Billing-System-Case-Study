import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
    customer_id,
    customer_name,
    address,
    meter_no,
    classification
FROM customers
""")

rows = cursor.fetchall()

print("\nCUSTOMER MASTER FILE")
print("=" * 60)

for row in rows:

    print(
        f"ID: {row[0]}"
    )

    print(
        f"Name: {row[1]}"
    )

    print(
        f"Address: {row[2]}"
    )

    print(
        f"Meter No: {row[3]}"
    )

    print(
        f"Class: {row[4]}"
    )

    print("-" * 60)

conn.close()