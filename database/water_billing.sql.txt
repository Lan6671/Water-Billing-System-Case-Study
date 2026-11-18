CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    address TEXT,
    meter_no TEXT,
    classification TEXT,
    status TEXT
);

CREATE TABLE meter_readings (
    reading_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    reading_date DATE,
    previous_reading INTEGER,
    current_reading INTEGER,
    consumption INTEGER
);

CREATE TABLE billings (
    bill_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    billing_month TEXT,
    consumption INTEGER,
    amount_due REAL,
    due_date DATE,
    bill_status TEXT
);

CREATE TABLE collections (
    collection_id INTEGER PRIMARY KEY,
    bill_id INTEGER,
    or_no TEXT,
    payment_date DATE,
    amount_paid REAL,
    collector TEXT
);