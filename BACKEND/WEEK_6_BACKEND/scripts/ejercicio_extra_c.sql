BEGIN;

SELECT stock FROM products WHERE id = 1;

UPDATE products
SET stock = stock - 1
WHERE id = 1
  AND stock = 1
RETURNING id;

INSERT INTO invoices(user_id, total_amount, status)
VALUES (1, 2000, 'pending')
RETURNING id;

INSERT INTO invoice_products(invoice_id, product_id, quantity, price, delivered)
VALUES (20, 1, 1, 2000, false);

COMMIT;

