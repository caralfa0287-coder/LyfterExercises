CREATE TABLE Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name UNIQUE NOT NULL,
    description TEXT
);

ALTER TABLE Products
	ADD COLUMN category_id INTEGER NULL REFERENCES Categories(id);

### Actualice algunos products asignándoles un category_id
UPDATE Products SET
	category_id = 1
WHERE code = 9012;

UPDATE Products SET
	category_id = 2
WHERE code = 1234;

### Establezca stock_available = 0 donde price <= 0
UPDATE Products
SET stock_available = 0
WHERE price <= 0;

### Aumente el price en 100 unidades para todos los productos cuando stock_available sea menor a 10
UPDATE Products
SET price = price + 100
WHERE stock_available < 10;

### Disminuya stock_available en 1 para un product_id específico
UPDATE Products
SET stock_available = stock_available - 1
WHERE code = 1234;

