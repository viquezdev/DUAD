insert into public.users (full_name, username, password) values
('Ana María Rodríguez', 'amrodriguez', 'pass123'),
('Luis Fernández', 'lufer', 'mypassword'),
('Carolina Soto', 'csoto', 'secret321'),
('José Ramírez', 'jramirez', 'qwerty'),
('María Gómez', 'mgomez', 'abcd1234');

insert into public.products (code, name, stock, price) values
('P001', 'Laptop Lenovo', 10, 850.00),
('P002', 'Mouse Inalámbrico', 50, 15.75),
('P003', 'Teclado Mecánico', 30, 55.90),
('P004', 'Monitor Samsung 24"', 20, 120.50),
('P005', 'Impresora HP', 15, 210.00);

insert into public.invoices (user_id, total_amount, status) values
(1, 865.75, 'pending'),
(2, 210.00, 'delivered'),
(3, 176.40, 'pending'),
(4, 120.50, 'returned'),
(5, 905.90, 'canceled');

insert into public.invoice_products (invoice_id, product_id, quantity, price, delivered) values
(1, 1, 1, 850.00, false),   
(1, 2, 1, 15.75, false),     
(2, 5, 1, 210.00, true),     
(3, 2, 2, 31.50, false),     
(3, 3, 1, 55.90, false),     
(4, 4, 1, 120.50, false),    
(5, 1, 1, 850.00, false),    
(5, 3, 1, 55.90, false);     


