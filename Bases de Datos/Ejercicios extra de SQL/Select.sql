### 
Verifique con SELECT * FROM products (muestre code, name, price, category_id, stock_available)
Select 
    code,
    name,
    price,
    category_id,
    stock_available
from Products;

### Seleccione todos los productos.
Select * 
from Products;

### Seleccione productos con price > 200
SELECT * 
FROM Products 
WHERE price > 200;

### Seleccione productos cuyo product_name contenga la palabra “saw” usando LIKE
SELECT *
FROM Products
WHERE name LIKE '%saw%';

### Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5
SELECT *
FROM Products
ORDER BY price DESC
LIMIT 5;

### Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10
SELECT *
FROM Products
ORDER BY code ASC
LIMIT 10;