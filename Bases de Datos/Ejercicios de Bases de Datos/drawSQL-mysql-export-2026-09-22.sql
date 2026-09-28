CREATE TABLE `Products`(
    `Code` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry date` DATE NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock available` INT NOT NULL
);
CREATE TABLE `Invoices`(
    `Invoice Number` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Purchase date` DATETIME NOT NULL,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Products per Invoice`(
    `Invoice number` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Product code` INT NOT NULL,
    `Quantity` INT NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    PRIMARY KEY(`Product code`)
);
CREATE TABLE `Shopping Cart`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Buyer email` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Shopping Cart` ADD UNIQUE `shopping cart_buyer email_unique`(`Buyer email`);
CREATE TABLE `Cart Items`(
    `Cart id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Product code` INT NOT NULL,
    `Quantity` INT NOT NULL,
    PRIMARY KEY(`Product code`)
);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_code_foreign` FOREIGN KEY(`Code`) REFERENCES `Cart Items`(`Cart id`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Products per Invoice`(`Invoice number`);
ALTER TABLE
    `Products per Invoice` ADD CONSTRAINT `products per invoice_invoice number_foreign` FOREIGN KEY(`Invoice number`) REFERENCES `Products`(`Name`);
ALTER TABLE
    `Cart Items` ADD CONSTRAINT `cart items_cart id_foreign` FOREIGN KEY(`Cart id`) REFERENCES `Shopping Cart`(`Buyer email`);



# Punto 5 Revisión de relaciones
Al revisar todas las tablas, he determinado que existen dos relaciones de muchos a muchos (N:N) que necesitan tablas intermedias para poder representarse correctamente.
La relación entre Invoices y Products es N:N, porque un invoice puede contener varios productos y un mismo producto puede aparecer en diferentes invoices. 
Para resolver esta relación se utiliza la tabla Products Per Invoice, que almacena la cantidad y el total de cada producto dentro de una factura.
La relación entre Shopping Cart y Products también es N:N, porque un carrito puede contener varios productos y un mismo producto puede estar en diferentes carritos. 
Esta relación se resuelve mediante la tabla Cart_Items, que almacena la cantidad de cada producto en el carrito.