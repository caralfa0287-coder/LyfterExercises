CREATE TABLE Products (
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    entry_date DATE NOT NULL,
    brand TEXT NOT NULL,
    stock_available INTEGER NOT NULL
);

CREATE TABLE Invoices (
    invoice_number INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date DATETIME NOT NULL,
    buyer_email TEXT NOT NULL,
    total_amount REAL NOT NULL
);

CREATE TABLE Products_Per_Invoice (
    invoice_number INTEGER REFERENCES Invoices(invoice_number),
    product_code INTEGER REFERENCES Products(code),
    quantity INTEGER NOT NULL,
    total_amount REAL NOT NULL,
    PRIMARY KEY (invoice_number)
);

CREATE TABLE Shopping_Cart (
    cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email TEXT NOT NULL UNIQUE
);

CREATE TABLE Cart_Items (
    cart_id INTEGER REFERENCES Shopping_Cart (cart_id),
    product_code INTEGER REFERENCES Products (code),
    quantity INTEGER NOT NULL
);

ALTER TABLE Invoices
ADD COLUMN employee_id INTEGER NOT NULL DEFAULT 0;

ALTER TABLE Invoices
ADD COLUMN phone_number INTEGER NOT NULL DEFAULT 0;

