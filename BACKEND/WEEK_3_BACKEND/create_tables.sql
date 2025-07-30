-- SQLite
CREATE TABLE products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	code VARCHAR(20) NOT NULL,
	name VARCHAR(25) NOT NULL,
	price FLOAT NOT NULL,
	entry_day DATETIME NOT NULL,
	brand VARCHAR(100) NOT NULL
);

CREATE TABLE shopping_cart (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	buyer_email VARCHAR(254) NOT NULL
);


CREATE TABLE invoices (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	number VARCHAR(20) NOT NULL,
	purchase_date DATETIME NOT NULL,
	buyer_email VARCHAR(254) NOT NULL,
	total_amount FLOAT NOT NULL,
	shopping_cart_id INTEGER UNIQUE REFERENCES shopping_cart(id)
);


CREATE TABLE invoices_products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	invoice_id INTEGER REFERENCES invoices(id),
	product_id INTEGER REFERENCES products(id),
	quantity INTEGER NOT NULL,
	total_amount FLOAT NOT NULL
	
);


CREATE TABLE shopping_cart_products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	shopping_cart_id INTEGER REFERENCES shopping_cart(id),
	product_id INTEGER REFERENCES products(id),
	quantity INTEGER NOT NULL
);




