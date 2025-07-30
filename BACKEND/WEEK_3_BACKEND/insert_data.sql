-- SQLite
--Products
INSERT INTO products(code,name,price,entry_day,brand)
    VALUES('P001','LAPTOP X200',150000,'2025-07-30 10:30:00','Lenovo');

INSERT INTO products(code,name,price,entry_day,brand)
    VALUES('P002','Mouse Pro',7500,'2025-07-30 10:30:00','Logitech');

INSERT INTO products(code,name,price,entry_day,brand)
    VALUES('P003','Teclado mecanico',22000,'2025-07-30 10:30:00','Redragon');

INSERT INTO products(code,name,price,entry_day,brand)
    VALUES('P004','Monitor 24"',95000,'2025-07-30 10:30:00','Samsung');

INSERT INTO products(code,name,price,entry_day,brand)
    VALUES('P005','LAPTOP X200',125000,'2025-07-30 10:30:00','Cougar');

--Shopping_cart

INSERT INTO shopping_cart(buyer_email)
    VALUES('juan@example.com');

INSERT INTO shopping_cart(buyer_email)
    VALUES('ana@example.com');

INSERT INTO shopping_cart(buyer_email)
    VALUES('carlos@example.com');

INSERT INTO shopping_cart(buyer_email)
    VALUES('maria@example.com');

INSERT INTO shopping_cart(buyer_email)
    VALUES('sofia@example.com');

--shopping_cart_products
INSERT INTO shopping_cart_products(shopping_cart_id,product_id,quantity)
    VALUES(1,1,1);

INSERT INTO shopping_cart_products(shopping_cart_id,product_id,quantity)
    VALUES(1,2,2);

INSERT INTO shopping_cart_products(shopping_cart_id,product_id,quantity)
    VALUES(2,3,1);

INSERT INTO shopping_cart_products(shopping_cart_id,product_id,quantity)
    VALUES(3,4,1);

INSERT INTO shopping_cart_products(shopping_cart_id,product_id,quantity)
    VALUES(4,5,1);

--Invoices

INSERT INTO invoices(number,purchase_date,buyer_email,total_amount,shopping_cart_id)
    VALUES('F1001','2025-07-10 10:00:00','juan@example.com',165000,1);

INSERT INTO invoices(number,purchase_date,buyer_email,total_amount,shopping_cart_id)
    VALUES('F1002','2025-07-11 12:00:00','ana@example.com',22000,2);

INSERT INTO invoices(number,purchase_date,buyer_email,total_amount,shopping_cart_id)
    VALUES('F1003','2025-07-12 14:00:00','carlos@example.com',95000,3);

INSERT INTO invoices(number,purchase_date,buyer_email,total_amount,shopping_cart_id)
    VALUES('F1004','2025-07-13 15:00:00','maria@example.com',125000,4);


--Invoices_products
INSERT INTO invoices_products(invoice_id,product_id,quantity,total_amount)
    VALUES(1,1,1,150000); 

INSERT INTO invoices_products(invoice_id,product_id,quantity,total_amount)
    VALUES(1,2,2,15000);

INSERT INTO invoices_products(invoice_id,product_id,quantity,total_amount)
    VALUES(2,3,1,22000);

INSERT INTO invoices_products(invoice_id,product_id,quantity,total_amount)
    VALUES(3,4,1,95000);

INSERT INTO invoices_products(invoice_id,product_id,quantity,total_amount)
    VALUES(4,5,1,125000);