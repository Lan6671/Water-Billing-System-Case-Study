import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
    bill_id,
    customer_id,
    billing_month,
    consumption,
    amount_due,
    due_date
FROM billings
""")

rows = cursor.fetchall()

print("\nBILLING FILE")
print("=" * 60)

for row in rows:

    print(f"Bill ID      : {row[0]}")
    print(f"Customer ID  : {row[1]}")
    print(f"Billing Month: {row[2]}")
    print(f"Consumption  : {row[3]}")
    print(f"Amount Due   : PHP {row[4]:,.2f}")
    print(f"Due Date     : {row[5]}")
    print("-" * 60)

conn.close()