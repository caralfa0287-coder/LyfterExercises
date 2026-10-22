CREATE TABLE `Owners`(
    `Owner_Id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Owner_Name` CHAR(255) NOT NULL,
    `Owner_Phone` BIGINT NOT NULL
);
CREATE TABLE `Insurances_Companies`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Insurance_Company` CHAR(255) NOT NULL
);
CREATE TABLE `Cars`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `VIN` TEXT NOT NULL,
    `Model_Id` BIGINT NOT NULL,
    `Color_Id` BIGINT NOT NULL,
    `Insurance_Policy_Id` BIGINT NOT NULL
);
CREATE TABLE `Models`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Make_Id` BIGINT NOT NULL,
    `Name` CHAR(255) NOT NULL,
    `Year_Id` BIGINT NOT NULL
);
CREATE TABLE `Makes`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` BIGINT NOT NULL
);
CREATE TABLE `Years`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Year` SMALLINT NOT NULL
);
CREATE TABLE `Colors`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` BIGINT NOT NULL
);
CREATE TABLE `Cars Owners`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Car_Id` BIGINT NOT NULL,
    `Owner_Id` BIGINT NOT NULL,
    `Is_Current` BOOLEAN NOT NULL
);
CREATE TABLE `Insurance_Policies`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Insurance_Company_Id` BIGINT NOT NULL,
    `Insurance_Policy` BIGINT NOT NULL
);
ALTER TABLE
    `Insurance_Policies` ADD CONSTRAINT `insurance_policies_insurance_company_id_foreign` FOREIGN KEY(`Insurance_Company_Id`) REFERENCES `Insurances_Companies`(`id`);
ALTER TABLE
    `Cars Owners` ADD CONSTRAINT `cars owners_car_id_foreign` FOREIGN KEY(`Car_Id`) REFERENCES `Cars`(`id`);
ALTER TABLE
    `Cars` ADD CONSTRAINT `cars_model_id_foreign` FOREIGN KEY(`Model_Id`) REFERENCES `Models`(`id`);
ALTER TABLE
    `Models` ADD CONSTRAINT `models_year_id_foreign` FOREIGN KEY(`Year_Id`) REFERENCES `Years`(`id`);
ALTER TABLE
    `Cars Owners` ADD CONSTRAINT `cars owners_owner_id_foreign` FOREIGN KEY(`Owner_Id`) REFERENCES `Owners`(`Owner_Id`);
ALTER TABLE
    `Cars` ADD CONSTRAINT `cars_color_id_foreign` FOREIGN KEY(`Color_Id`) REFERENCES `Colors`(`id`);
ALTER TABLE
    `Models` ADD CONSTRAINT `models_make_id_foreign` FOREIGN KEY(`Make_Id`) REFERENCES `Makes`(`id`);

--1FN: Cada columna contiene valores individuales: un VIN, una marca, un modelo, un propietario, etc. No hay listas de propietarios o seguros dentro de una misma celda. Por tanto, la tabla ya cumple la 1FN.

--2FN: eliminamos dependencias parciales separando carros, modelos, colores, marcas, compañías de seguros y propietarios. La tabla Cars_Owners conserva la relación entre vehiculos y propietarios, ademas de un indicador de si el propietario es el actual. 

--3FN: separamos las compañías y pólizas de seguros, la información de cada compañía se almacena una sola vez y las pólizas se registran en una tabla independiente vinculando la Poliza al vehiculo. Cars_Owners conserva únicamente las claves necesarias para relacionar vehículos y propietarios.

--Conclusión: La normalización de la base de datos garantiza que cada entidad (vehículos, propietarios, modelos, colores, marcas y seguros) tenga su propia tabla, eliminando redundancias y dependencias innecesarias. Esto facilita la gestión de datos y asegura la integridad referencial entre las tablas.