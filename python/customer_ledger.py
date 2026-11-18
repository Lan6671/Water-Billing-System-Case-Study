import sqlite3

conn = sqlite3.connect("../water_billing.db")

cursor = conn.cursor()

cursor.execute("""

SELECT

c.customer_name,

b.amount_due,

IFNULL(
    SUM(col.amount_paid),
    0
) AS total_paid,

b.amount_due -
IFNULL(
    SUM(col.amount_paid),
    0
) AS balance

FROM billings b

INNER JOIN customers c
ON b.customer_id = c.customer_id

LEFT JOIN collections col
ON b.bill_id = col.bill_id

GROUP BY
c.customer_name,
b.amount_due

""")

rows = cursor.fetchall()

print("\nCUSTOMER LEDGER")
print("=" * 70)

for row in rows:

    print(
        f"Customer : {row[0]}"
    )

    print(
        f"Bill Amount : PHP {row[1]:,.2f}"
    )

    print(
        f"Payments : PHP {row[2]:,.2f}"
    )

    print(
        f"Balance : PHP {row[3]:,.2f}"
    )

    print("-" * 50)

conn.close()