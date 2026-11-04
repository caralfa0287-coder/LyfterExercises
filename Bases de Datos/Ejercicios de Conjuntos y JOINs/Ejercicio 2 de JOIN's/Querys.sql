-- 1. Obtenga todos los libros y sus autores (en caso de tenerlos)
SELECT
    Books.ID,
    Books.Name AS Book,
    Authors.Name AS Author
FROM Books
LEFT JOIN Authors
    ON Books.Author = Authors.ID;

-- 2. Obtenga todos los libros que no tienen autor
SELECT ID, Name
FROM Books
WHERE Author IS NULL;

-- 3. Obtenga todos los autores que no tienen libros
SELECT
    Authors.ID,
    Authors.Name
FROM Authors
LEFT JOIN Books
    ON Authors.ID = Books.Author
WHERE Books.ID IS NULL;

-- 4. Obtenga todos los libros que han sido rentados en algún momento
SELECT DISTINCT
    Books.ID,
    Books.Name
FROM Books
INNER JOIN Rents
    ON Books.ID = Rents.BookID;

-- 5. Obtenga todos los libros que nunca han sido rentados
SELECT
    Books.ID,
    Books.Name
FROM Books
LEFT JOIN Rents
    ON Books.ID = Rents.BookID
WHERE Rents.ID IS NULL;

-- 6. Obtenga todos los clientes que nunca han rentado un libro
SELECT
    Customers.ID,
    Customers.Name,
    Customers.Email
FROM Customers
LEFT JOIN Rents
    ON Customers.ID = Rents.CustomerID
WHERE Rents.ID IS NULL;

-- 7. Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT DISTINCT
    Books.ID,
    Books.Name
FROM Books
INNER JOIN Rents
    ON Books.ID = Rents.BookID
WHERE Rents.State = 'Overdue';