import pandas as pd

RATE_PER_CUBIC = 25

# Read customer data
df = pd.read_csv("../customers.csv")

# Compute consumption
df["consumption"] = (
    df["current_reading"]
    - df["previous_reading"]
)

# Compute billing
df["amount_due"] = (
    df["consumption"]
    * RATE_PER_CUBIC
)

# Display Report
print("\nWATER BILLING REPORT")
print("=" * 60)

for _, row in df.iterrows():

    print(
        f"{row['customer_name']}"
    )

    print(
        f"Consumption : {row['consumption']}"
    )

    print(
        f"Amount Due   : PHP {row['amount_due']:,.2f}"
    )

    print("-" * 40)

total_revenue = df["amount_due"].sum()

print(
    f"\nTOTAL REVENUE : PHP {total_revenue:,.2f}"
)

# Export Excel Report
df.to_excel(
    "../billing_report.xlsx",
    index=False
)

print(
    "\nExcel Report Generated: billing_report.xlsx"
)