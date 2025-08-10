-- SQLite


-- Get all books and their authors

SELECT books.name, authors.name
FROM books
INNER JOIN authors
ON books.author_id = authors.id;

-- Get all books that do not have an author

SELECT books.name
FROM books
LEFT JOIN authors
ON books.author_id = author_id
WHERE authors.id IS NULL;

-- Get all authors who do not have books

SELECT authors.name
FROM authors
LEFT JOIN books
ON authors.id = books.author_id
WHERE books.id IS NULL;

--Get all books that have been rented at some point
SELECT DISTINCT books.name
FROM rents
INNER JOIN books
ON rents.book_id = books.id;

--Get all books that have never been rented
SELECT books.name
FROM books
LEFT JOIN rents
ON books.id=rents.book_id
WHERE rents.id IS NULL;

--Get all customers who have never rented a book
SELECT customers.name
FROM customers
LEFT JOIN rents
ON customers.id=rents.customer_id
WHERE rents.id IS NULL;

--Get all books that have been rented and are in “Overdue” status
SELECT books.name
FROM books
INNER JOIN rents
ON books.id=rents.book_id
WHERE rents.state='Overdue';