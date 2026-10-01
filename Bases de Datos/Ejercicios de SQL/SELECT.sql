###Obtenga todos los productos almacenados
SELECT *
	FROM Products;

###Obtenga todos los productos que tengan un precio mayor a 250
SELECT *
	FROM Products
    WHERE price > 250

###Obtenga todas las compras de un mismo producto por id.
SELECT *
FROM Products_Per_Invoice
WHERE product_code = 1234;

###Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT 
    product_code,
    SUM(quantity) AS total_buyed
FROM Products_Per_Invoice
GROUP BY product_code;

###Obtenga todas las facturas realizadas por el mismo comprador
SELECT *
FROM Invoices
WHERE buyer_email = 'caralfa@example.com';

###Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT *
FROM Invoices
ORDER BY total_amount DESC;

###Obtenga una sola factura por número de factura.
SELECT *
FROM Invoices
WHERE invoice_number = 1;