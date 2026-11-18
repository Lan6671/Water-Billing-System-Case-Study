import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
reading_id,
customer_id,
reading_date,
consumption
FROM meter_readings
""")

rows = cursor.fetchall()

print("\nMETER READING FILE")
print("=" * 50)

for row in rows:

    print(
        f"Reading ID : {row[0]}"
    )

    print(
        f"Customer ID : {row[1]}"
    )

    print(
        f"Reading Date : {row[2]}"
    )

    print(
        f"Consumption : {row[3]}"
    )

    print("-" * 40)

conn.close()