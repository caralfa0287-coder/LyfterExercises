CREATE TABLE `Customers`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `customer_name` CHAR(255) NOT NULL,
    `customer_phone` CHAR(255) NOT NULL
);
CREATE TABLE `Items`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `item_name` CHAR(255) NOT NULL,
    `price` TEXT NOT NULL
);
CREATE TABLE `Orders`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `customer_id` BIGINT NOT NULL,
    `delivery_time` TIME NOT NULL,
    `address` TEXT NOT NULL
);

-- Tabla intermedia entre pedidos y productos
CREATE TABLE `items_per_order`(
    `order_id` BIGINT UNSIGNED NOT NULL,
    `item_id` BIGINT NOT NULL,
    `quantity` SMALLINT NOT NULL,
    `special_request` TEXT NULL,
    PRIMARY KEY(`order_id`, `item_id`)
);
ALTER TABLE
    `items_per_order` ADD CONSTRAINT `items_per_order_item_id_foreign` FOREIGN KEY(`item_id`) REFERENCES `Items`(`id`);
ALTER TABLE
    `items_per_order` ADD CONSTRAINT `items_per_order_order_id_foreign` FOREIGN KEY(`order_id`) REFERENCES `Orders`(`id`);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_customer_id_foreign` FOREIGN KEY(`customer_id`) REFERENCES `Customers`(`id`);


--1FN = no es necesario modificar la tabla para alcanzar la 1FN, pero sí hay que separar los datos para avanzar hacia formas normales superiores. No hay celdas con listas de productos ni grupos de columnas repetidas.
--2FN = Dividimos la tabla original en tres tablas. Los datos del pedido se guardan en Orders, los datos del producto en Items y los datos de cada cliente dentro de Customers. Así eliminamos las dependencias parciales de la clave compuesta.
--Tabla Orders: Contiene los atributos que dependen de Order ID.
--Tabla Items: Contiene los atributos que dependen de Item ID.
--Tabla Customers: Contiene los atributos que dependen de Customer ID.
--Tabla intermedia items_per_order: Contiene los atributos que dependen de la clave compuesta (Order ID, Item ID).
--3FN = La información del cliente no debería repetirse en cada pedido. Por eso creamos una tabla independiente para los clientes. El esquema final queda formado por cuatro tablas.

--Conclusión: la 1FN garantiza valores atómicos, la 2FN elimina dependencias parciales y la 3FN elimina dependencias transitivas. El resultado es una base de datos organizada, con menos duplicación y con relaciones claras entre clientes, pedidos y productos.