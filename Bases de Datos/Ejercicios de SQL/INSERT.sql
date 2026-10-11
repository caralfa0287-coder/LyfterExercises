INSERT INTO Products (name, price, entry_date, brand, stock_available)
	VALUES ('Hammer', 34.99, '2026-06-01', 'Makita', 5);

INSERT INTO Products (name, price, entry_date, brand, stock_available)
	VALUES ('Drill', 49.99, '2026-06-02', 'DeWalt', 10);

INSERT INTO Products (name, price, entry_date, brand, stock_available)
	VALUES ('TableSaw', 5198.50, '2026-06-03', 'Bosch', 2);

INSERT INTO Products (name, price, entry_date, brand, stock_available)
	VALUES ('Chainsaw', 299.99, '2026-06-04', 'Stihl', 7);

INSERT INTO Products (name, price, entry_date, brand, stock_available)
	VALUES ('Mower', 3455.99, '2026-06-01', 'Makita', 2);
	
INSERT INTO Invoices (invoice_number, purchase_date, buyer_email, total_amount, employee_id, phone_number)
	VALUES (00001, '2026-07-05', 'caralfa@example.com', 334.98, 0035, '+0018432272707');

INSERT INTO Invoices (invoice_number, purchase_date, buyer_email, total_amount, employee_id, phone_number)
	VALUES (00002, '2026-07-06', 'andresbuyer@example.com', 5283.48, 0042, '+0018432272708');

INSERT INTO Products_Per_Invoice (invoice_number, product_code, quantity, total_amount)
	VALUES (00001, 1234, 1, 34.99);

INSERT INTO Products_Per_Invoice (invoice_number, product_code, quantity, total_amount)
	VALUES (00002, 5678, 1, 49.99);

INSERT INTO Products_Per_Invoice (invoice_number, product_code, quantity, total_amount)
	VALUES (00001, 3456, 1, 299.99);

INSERT INTO Products_Per_Invoice (invoice_number, product_code, quantity, total_amount)
	VALUES (00002, 9012, 1, 5198.50);

INSERT INTO Shopping_Cart (cart_id, buyer_email)
	VALUES (00001, 'caralfa@example.com');

INSERT INTO Shopping_Cart (cart_id, buyer_email)
	VALUES (00002, 'andresbuyer@example.com');

INSERT INTO Cart_Items(cart_id, product_code, quantity)
	VALUES (00001, 1234, 1);

INSERT INTO Cart_Items(cart_id, product_code, quantity)
	VALUES (00002, 5678, 1);

INSERT INTO Cart_Items(cart_id, product_code, quantity)
	VALUES (00001, 3456, 1);

INSERT INTO Cart_Items(cart_id, product_code, quantity)
	VALUES (00001, 9012, 1);