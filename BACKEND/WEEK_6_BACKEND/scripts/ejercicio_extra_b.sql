BEGIN;

SELECT id,stock
FROM public.products
WHERE (id=1 AND stock <3)
	OR(id=2 AND stock <2)

INSERT INTO public.invoices(user_id, total_amount, status)
VALUES (1, 0, 'pending')
RETURNING id;

INSERT INTO public.invoice_products(invoice_id, product_id, quantity, price, delivered)
VALUES
(10, 1, 3, 2000, false),
(10, 2, 2, 1500, false);

UPDATE public.products
SET stock = stock - 3
WHERE id = 1;

UPDATE public.products
SET stock = stock - 2
WHERE id = 2;

UPDATE invoices
SET total_amount = (
  SELECT SUM(quantity * price)
  FROM invoice_products
  WHERE invoice_id = 10
)
WHERE id = 10;

COMMIT;