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
    `Total amount` DECIMAL(8, 2) NOT NULL,
    `Method id` INT NOT NULL
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
CREATE TABLE `Reviews`(
    `Review id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Product code` INT NOT NULL,
    `User id` INT NOT NULL,
    `Comment` TEXT NOT NULL,
    `Rating` TINYINT NOT NULL,
    `Review date` DATETIME NOT NULL
);
CREATE TABLE `Payment Methods`(
    `Method id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Method type` VARCHAR(255) NOT NULL,
    `Bank name` VARCHAR(255) NULL
);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_review id_foreign` FOREIGN KEY(`Review id`) REFERENCES `Users`(`User id`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_invoice number_foreign` FOREIGN KEY(`Method id`) REFERENCES `Payment Methods`(`Method id`);
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
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_review id_foreign` FOREIGN KEY(`Review id`) REFERENCES `Products`(`Code`);


### Pregunta reflexiva:
¿Cada factura debe tener exactamente un método de pago, o podría haber más de uno?
R. Para funcion de este ejercicio se puede establecer que cada factura tiene exactamente un método de pago. Por esta razón, no es necesario utilizar una tabla intermedia
y se puede agregar method_id como clave foránea directamente en Invoices.
La relación entre Payment_Methods e Invoices sería de 1:N, ya que un método de pago puede utilizarse en muchas facturas, pero cada factura utiliza un solo método de pago. 
Si el sistema permitiera dividir un pago entre varios métodos, entonces sería necesario utilizar una tabla intermedia para representar una relación N:N.