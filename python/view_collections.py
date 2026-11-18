import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
collection_id,
bill_id,
or_no,
payment_date,
amount_paid
FROM collections
""")

rows = cursor.fetchall()

print("\nCOLLECTION FILE")
print("=" * 50)

for row in rows:

    print(f"Collection ID : {row[0]}")
    print(f"Bill ID       : {row[1]}")
    print(f"OR Number     : {row[2]}")
    print(f"Payment Date  : {row[3]}")
    print(f"Amount Paid   : PHP {row[4]:,.2f}")

    print("-" * 40)

conn.close()