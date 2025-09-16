BEGIN;

UPDATE public.invoices SET status='canceled'
WHERE id=3 AND status='pending'
RETURNING id;

UPDATE public.products p
SET stock=stock + ip.quantity
FROM public.invoice_products ip
WHERE ip.invoice_id=3
	AND ip.product_id=p.id
	AND ip.delivered=false;

COMMIT;
