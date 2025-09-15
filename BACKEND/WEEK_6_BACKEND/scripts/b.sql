BEGIN;

SELECT stock FROM public.products WHERE id = 1 FOR UPDATE;
SELECT stock FROM public.products WHERE id = 2 FOR UPDATE;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM public.users WHERE id = 1) THEN
        RAISE EXCEPTION 'User with id=1 does not exist';
    END IF;
END;
$$;


WITH new_invoice AS (
    INSERT INTO public.invoices(user_id, total_amount, status)
    VALUES (1, 0, 'pending')
    RETURNING id
)

INSERT INTO public.invoice_products(invoice_id, product_id, quantity, price, delivered)
SELECT id, 1, 3, 2550.00, false FROM new_invoice
UNION ALL
SELECT id, 2, 2, 31.50, false FROM new_invoice;

UPDATE public.products
SET stock = stock - 3
WHERE id = 1 AND stock >= 3;

UPDATE public.products
SET stock = stock - 2
WHERE id = 2 AND stock >= 2;

UPDATE public.invoices
SET total_amount = (
    SELECT SUM(quantity * price)
    FROM public.invoice_products
    WHERE invoice_id = (SELECT id FROM public.invoices ORDER BY id DESC LIMIT 1)
)
WHERE id =(SELECT id FROM public.invoices ORDER BY id DESC LIMIT 1);;

COMMIT;
