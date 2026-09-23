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
CREATE TABLE `Reviews`(
    `Review id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Product code` INT NOT NULL,
    `User id` INT NOT NULL,
    `Comment` TEXT NOT NULL,
    `Rating` TINYINT NOT NULL,
    `Review date` DATETIME NOT NULL
);
ALTER TABLE
    `Reviews` ADD CONSTRAINT `reviews_review id_foreign` FOREIGN KEY(`Review id`) REFERENCES `Users`(`User id`);
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
¿Una reseña puede existir sin un producto o sin un usuario?
R. No, una reseña no puede existir sin un producto o sin un usuario. Esto se debe a que las reseñas están vinculadas tanto a un producto específico como a un usuario que la realiza.
En la estructura de la base de datos, las claves foráneas en la tabla `Reviews` aseguran que cada reseña esté asociada a un producto (`Product code`) y a un usuario (`User id`).
Por lo tanto, si se intenta crear una reseña sin un producto o sin un usuario válido, la base de datos no permitirá la inserción debido a las restricciones de integridad referencial.