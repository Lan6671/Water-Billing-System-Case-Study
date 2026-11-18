import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

# Total Billing
cursor.execute("""
SELECT
SUM(amount_due)
FROM billings
""")

total_billing = cursor.fetchone()[0]

# Total Collection
cursor.execute("""
SELECT
SUM(amount_paid)
FROM collections
""")

total_collection = cursor.fetchone()[0]

if total_collection is None:
    total_collection = 0

# Outstanding Balance
outstanding = (
    total_billing
    - total_collection
)

# Collection Efficiency
efficiency = (
    total_collection
    / total_billing
) * 100

print("\nCOLLECTION MONITORING REPORT")
print("=" * 60)

print(
    f"Total Billing     : PHP {total_billing:,.2f}"
)

print(
    f"Total Collection  : PHP {total_collection:,.2f}"
)

print(
    f"Outstanding       : PHP {outstanding:,.2f}"
)

print(
    f"Collection Rate   : {efficiency:.2f}%"
)

conn.close()