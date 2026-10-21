CREATE TABLE `Customers`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `customer_name` CHAR(255) NOT NULL,
    `customer_phone` CHAR(255) NOT NULL,
    `address` TEXT NOT NULL
);
CREATE TABLE `Items`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `item_name` CHAR(255) NOT NULL,
    `price` TEXT NOT NULL
);
CREATE TABLE `Orders`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `customer_id` BIGINT NOT NULL,
    `delivery_time` TIME NOT NULL
);
CREATE TABLE `items_per_order`(
    `order_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `item_id` BIGINT NOT NULL,
    `quantity` SMALLINT NOT NULL,
    `special_request` BIGINT NOT NULL,
    PRIMARY KEY(`item_id`)
);
ALTER TABLE
    `items_per_order` ADD CONSTRAINT `items_per_order_item_id_foreign` FOREIGN KEY(`item_id`) REFERENCES `Items`(`id`);
ALTER TABLE
    `items_per_order` ADD CONSTRAINT `items_per_order_order_id_foreign` FOREIGN KEY(`order_id`) REFERENCES `Orders`(`id`);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_customer_id_foreign` FOREIGN KEY(`customer_id`) REFERENCES `Customers`(`id`);