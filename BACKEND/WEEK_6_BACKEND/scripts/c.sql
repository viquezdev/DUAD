BEGIN;

SELECT id FROM public.invoices WHERE id=11 FOR UPDATE;

UPDATE public.products
SET stock=stock+3
WHERE id=1 
RETURNING id;

UPDATE public.products
SET stock=stock+2
WHERE id=2 
RETURNING id;

UPDATE public.invoices
SET status = 'returned'
WHERE id=11
RETURNING id;

COMMIT;
