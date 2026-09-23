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
    `User id` INT NOT NULL,
    `Purchase date` DATETIME NOT NULL,
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
CREATE TABLE `Users`(
    `User id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Full name` VARCHAR(255) NOT NULL,
    `Email` VARCHAR(255) NOT NULL,
    `Registration Date` DATETIME NOT NULL
);
ALTER TABLE
    `Users` ADD UNIQUE `users_email_unique`(`Email`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_code_foreign` FOREIGN KEY(`Code`) REFERENCES `Cart Items`(`Cart id`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Products per Invoice`(`Invoice number`);
ALTER TABLE
    `Products per Invoice` ADD CONSTRAINT `products per invoice_invoice number_foreign` FOREIGN KEY(`Invoice number`) REFERENCES `Products`(`Name`);
ALTER TABLE
    `Cart Items` ADD CONSTRAINT `cart items_cart id_foreign` FOREIGN KEY(`Cart id`) REFERENCES `Shopping Cart`(`Buyer email`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_user id_foreign` FOREIGN KEY(`User id`) REFERENCES `Users`(`User id`);


## Preguntas reflexivas:
¿Cada factura debe tener relación con un usuario, o puede existir una factura sin cuenta?
R. Cada factura debe tener relación con un usuario, ya que el usuario es quien realiza la compra, no puede existir una factura sin un usuario asociado.
¿Necesita una tabla intermedia? ¿Por qué?
R. No, porque hay una relación uno a muchos entre usuario y facturas. Un usuario puede terner muchas facturas, pero una factura solo puede pertenecer a un usuario.
Ahora se relaciona mediante el id del usuario, ¿es necesario mantener el correo del usuario como en el ejercicio anterior?
R. No, ya que el id del usuario es suficiente para identificar al usuario.